# Generated by Django 4.1.7 on 2023-06-16 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("operators", "0005_alter_operator_current_ticket"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="operator",
            name="current_ticket",
        ),
    ]
