# Generated by Django 2.0.3 on 2020-03-14 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('name', models.CharField(max_length=200, verbose_name='名称')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='描述')),
            ],
            options={
                'verbose_name': '测试用例',
                'verbose_name_plural': '测试用例',
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
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cases.TestCase', verbose_name='测试用例')),
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
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project', verbose_name='项目')),
            ],
            options={
                'verbose_name': '测试套件',
                'verbose_name_plural': '测试套件',
            },
        ),
        migrations.AddField(
            model_name='testcase',
            name='suite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cases.TestSuite', verbose_name='测试套件'),
        ),
    ]
