# Generated by Django 3.2.12 on 2022-03-12 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_tododata_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='tododata',
            name='desc',
            field=models.TextField(null=True),
        ),
    ]