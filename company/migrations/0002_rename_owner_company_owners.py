# Generated by Django 5.0.3 on 2024-03-12 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='owner',
            new_name='owners',
        ),
    ]
