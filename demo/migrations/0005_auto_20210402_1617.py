# Generated by Django 3.1.7 on 2021-04-02 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0004_auto_20210402_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='email',
            field=models.TextField(max_length=50),
        ),
    ]
