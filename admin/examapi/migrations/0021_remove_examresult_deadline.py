# Generated by Django 5.1.4 on 2024-12-29 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('examapi', '0020_examresult_deadline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examresult',
            name='deadline',
        ),
    ]