# Generated by Django 5.1.4 on 2024-12-29 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examapi', '0013_examresult_deadline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examresult',
            name='deadline',
        ),
        migrations.AddField(
            model_name='examresult',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
    ]
