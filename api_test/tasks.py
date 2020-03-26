from celery import shared_task
import requests

from utils.runner import run_step


@shared_task
def delay(x, y):
    print(f'sum is {x+y}')
    return x + y


@shared_task
def run(data):
    result = run_step(data)
    return result
