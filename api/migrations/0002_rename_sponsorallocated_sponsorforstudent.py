# Generated by Django 5.0.1 on 2024-01-29 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SponsorAllocated',
            new_name='SponsorForStudent',
        ),
    ]
