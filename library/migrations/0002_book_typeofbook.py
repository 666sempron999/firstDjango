# Generated by Django 2.0 on 2019-05-17 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='typeOfBook',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
