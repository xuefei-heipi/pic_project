# Generated by Django 2.1.11 on 2019-12-27 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0017_jsignore'),
    ]

    operations = [
        migrations.AddField(
            model_name='teststatus',
            name='fastCheckPassword',
            field=models.CharField(default='----', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teststatus',
            name='fastCheckUsername',
            field=models.CharField(default='---', max_length=30),
            preserve_default=False,
        ),
    ]