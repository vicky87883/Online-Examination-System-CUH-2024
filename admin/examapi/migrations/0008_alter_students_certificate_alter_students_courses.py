# Generated by Django 5.1.3 on 2024-12-03 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examapi', '0007_apikeys'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='certificate',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='students',
            name='courses',
            field=models.CharField(max_length=255),
        ),
    ]
