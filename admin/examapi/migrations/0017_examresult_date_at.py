# Generated by Django 5.1.4 on 2024-12-29 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examapi', '0016_remove_examresult_uploaded_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='examresult',
            name='date_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
