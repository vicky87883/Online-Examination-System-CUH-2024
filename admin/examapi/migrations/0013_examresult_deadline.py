# Generated by Django 5.1.4 on 2024-12-29 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examapi', '0012_remove_examresult_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='examresult',
            name='deadline',
            field=models.DateField(null=True),
        ),
    ]