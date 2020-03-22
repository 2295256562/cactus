# Generated by Django 2.0.3 on 2020-03-22 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Api',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('name', models.CharField(max_length=200, verbose_name='名称')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='描述')),
                ('path', models.CharField(max_length=200, verbose_name='接口路径')),
                ('method', models.CharField(choices=[('get', 'GET'), ('post', 'POST'), ('put', 'PUT'), ('delete', 'DELETE'), ('head', 'HEAD'), ('patch', 'PATCH'), ('options', 'OPTIONS')], default='get', max_length=10, verbose_name='请求方法')),
            ],
            options={
                'verbose_name': '接口',
                'verbose_name_plural': '接口',
            },
        ),
        migrations.CreateModel(
            name='ApiCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('name', models.CharField(max_length=200, verbose_name='名称')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='描述')),
            ],
            options={
                'verbose_name': '接口分类',
                'verbose_name_plural': '接口分类',
            },
        ),
        migrations.CreateModel(
            name='Env',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('name', models.CharField(max_length=200, verbose_name='名称')),
                ('base_url', models.CharField(blank=True, max_length=500, null=True, verbose_name='域名')),
                ('request', models.TextField(blank=True, null=True, verbose_name='请求more配置')),
            ],
            options={
                'verbose_name': '环境',
                'verbose_name_plural': '环境',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('name', models.CharField(max_length=200, verbose_name='名称')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='描述')),
            ],
            options={
                'verbose_name': '项目',
                'verbose_name_plural': '项目',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('name', models.CharField(max_length=200, verbose_name='名称')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='描述')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_test.Project', verbose_name='项目')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('name', models.CharField(max_length=200, verbose_name='名称')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='描述')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_test.Project', verbose_name='项目')),
                ('tags', models.ManyToManyField(blank=True, null=True, to='api_test.Tag', verbose_name='标签')),
            ],
            options={
                'verbose_name': '测试用例',
                'verbose_name_plural': '测试用例',
            },
        ),
        migrations.CreateModel(
            name='TestReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('name', models.CharField(max_length=200, verbose_name='名称')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='描述')),
                ('content', models.TextField(verbose_name='报告内容')),
                ('case', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api_test.TestCase', verbose_name='测试用例')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_test.Project', verbose_name='项目')),
            ],
            options={
                'verbose_name': '测试步骤',
                'verbose_name_plural': '测试步骤',
            },
        ),
        migrations.CreateModel(
            name='TestStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('name', models.CharField(max_length=200, verbose_name='名称')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='描述')),
                ('order', models.IntegerField(verbose_name='步骤顺序')),
                ('skip', models.BooleanField(default=False, verbose_name='跳过用例')),
                ('request', models.TextField(verbose_name='请求数据')),
                ('extract', models.TextField(verbose_name='提取数据')),
                ('check', models.TextField(verbose_name='断言数据')),
                ('api', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_test.Api', verbose_name='接口')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='api_test.TestCase', verbose_name='测试用例')),
            ],
            options={
                'verbose_name': '测试步骤',
                'verbose_name_plural': '测试步骤',
            },
        ),
        migrations.CreateModel(
            name='TestSuite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('name', models.CharField(max_length=200, verbose_name='名称')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='描述')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_test.Project', verbose_name='项目')),
                ('suite', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_suites', to='api_test.TestSuite', verbose_name='父级套件')),
                ('testcases', models.ManyToManyField(blank=True, to='api_test.TestCase', verbose_name='测试用例')),
            ],
            options={
                'verbose_name': '测试套件',
                'verbose_name_plural': '测试套件',
            },
        ),
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('key', models.CharField(max_length=200, verbose_name='变量')),
                ('value', models.CharField(max_length=500, verbose_name='变量值')),
                ('env', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='env_variables', to='api_test.Env', verbose_name='环境')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_variables', to='api_test.Project', verbose_name='项目')),
            ],
            options={
                'verbose_name': '环境变量',
                'verbose_name_plural': '环境变量',
            },
        ),
        migrations.AddField(
            model_name='testreport',
            name='step',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api_test.TestStep', verbose_name='测试步骤'),
        ),
        migrations.AddField(
            model_name='testreport',
            name='suite',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api_test.TestSuite', verbose_name='测试套件'),
        ),
        migrations.AddField(
            model_name='env',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_test.Project', verbose_name='项目'),
        ),
        migrations.AddField(
            model_name='apicategory',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_test.Project', verbose_name='项目'),
        ),
        migrations.AddField(
            model_name='api',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api_test.ApiCategory', verbose_name='接口组'),
        ),
        migrations.AddField(
            model_name='api',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_test.Project', verbose_name='项目'),
        ),
    ]
