# Generated by Django 5.0 on 2024-02-27 21:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("chat", "0002_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="message",
            name="from_chat",
        ),
        migrations.RemoveField(
            model_name="message",
            name="user",
        ),
        migrations.DeleteModel(
            name="Chat",
        ),
        migrations.DeleteModel(
            name="Message",
        ),
    ]