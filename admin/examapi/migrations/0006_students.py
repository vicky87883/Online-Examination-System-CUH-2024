# Generated by Django 5.1.3 on 2024-12-03 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examapi', '0005_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('students', models.CharField(max_length=255)),
                ('emailid', models.CharField(max_length=255)),
                ('courses', models.DateField()),
                ('certificate', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], max_length=50)),
                ('actions', models.TextField()),
            ],
        ),
    ]