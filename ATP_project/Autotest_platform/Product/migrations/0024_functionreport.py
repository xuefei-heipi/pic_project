# Generated by Django 2.1.11 on 2020-03-11 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0023_functiontest_testname'),
    ]

    operations = [
        migrations.CreateModel(
            name='FunctionReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reportName', models.CharField(max_length=200)),
                ('type', models.IntegerField()),
            ],
            options={
                'db_table': 'FunctionReport',
            },
        ),
    ]