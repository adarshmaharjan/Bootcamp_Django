# Generated by Django 3.2.5 on 2021-08-09 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_relation', '0005_information'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='bio',
            field=models.TextField(),
        ),
    ]
