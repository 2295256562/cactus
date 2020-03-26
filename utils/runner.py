import os
import json
from string import Template
from collections import ChainMap

import yaml
from logz import log
import requests


def yaml2dict(text, default={}):
    try:
        return yaml.safe_load(text)
    except Exception as ex:
        log.exception(ex)
        return default

def render(text, context):
    return Template(text).safe_substitute(context)


def do_extract(text, context):
    _extract = yaml2dict(text)
    for key, expr in _extract.items():
        result = eval(expr, {}, context)
        log.info(f'提取: {key}={expr} 结果: {result}')
        context[key] = result


def do_check(text, context):
    _check = yaml2dict(text)
    result = True
    for expr in _check:
        result = eval(expr, {}, context)
        log.info(f'断言: {expr} 结果: {result}')
    return 'PASS' if result else 'FAIL'


def do_config(config, session, context):
    variables = config.get('variables')
    request = config.get('request')

    if variables and isinstance(variables, dict):
        context.update(variables)
    if request:
        for key, value in request.items():
            setattr(session, key, value)



def run_step(data, session=None, context=None, config=None, debug=False):
    session = session or requests.session()
    context = context or ChainMap({}, os.environ)

    name = data.get('name')
    config = data.get('config')
    request = data.get('request')

    log.info(f'执行步骤: {name}')

    if config:
        base_url = config.get('base_url')
        if base_url:
            url = request.get('url', '')
            if not url.startswith('http'):
                request['url'] = '/'.join((base_url.rstrip('/'), url.lstrip('/')))

    log.info(f'发送请求: {request}')
    status = 'PASS'
    try:
        response = session.request(**request)
        log.info(f'响应数据: {response.text}')
    except Exception as ex:
        log.exception(ex)
        status = 'ERROR'
        return dict(status=status, exec_info=str(ex))


    extract = data.get('extract')
    check = data.get('check')
    if extract:
        do_extract(extract, context)

    if check:
        status = do_check(check, context)

    result = dict(status=status,
                  status_code=response.status_code,
                  response_text=response.text,
                  response_headers=dict(response.headers),
                  response_time=response.elapsed.seconds)
    context.update(result)
    return result


def run_case(data, session=None, context=None, debug=False):
    session = session or requests.session()
    context = context or ChainMap({}, os.environ)

    name = data.get('name')
    description = data.get('description')

    config = data.get('config',{})
    steps = data.get('steps')
    # todo