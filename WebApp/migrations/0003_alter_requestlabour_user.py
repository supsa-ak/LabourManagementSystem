# Generated by Django 4.1.3 on 2022-11-20 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0002_alter_requestlabour_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestlabour',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]
