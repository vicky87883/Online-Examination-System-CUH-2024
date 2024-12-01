# Generated by Django 5.0.7 on 2024-12-01 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APIKeys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('students', models.CharField(max_length=255)),
                ('lesson', models.CharField(max_length=255)),
                ('deadline', models.DateField()),
                ('sent', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], max_length=50)),
                ('actions', models.TextField()),
            ],
        ),
    ]