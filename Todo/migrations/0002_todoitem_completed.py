# Generated by Django 5.0.6 on 2024-07-31 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
