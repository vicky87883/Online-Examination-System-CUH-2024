# Generated by Django 5.1.4 on 2024-12-29 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examapi', '0019_remove_examresult_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='examresult',
            name='deadline',
            field=models.DateField(null=True),
        ),
    ]