# Generated by Django 4.1 on 2022-11-18 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hommie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='available',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='property',
            name='propertyimage',
            field=models.FileField(upload_to='covers/'),
        ),
    ]
