# Generated by Django 2.0 on 2017-12-22 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producers', '0001_initial'),
        ('competitions', '0006_competition_remote_id'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='competition',
            unique_together={('remote_id', 'producer')},
        ),
    ]
