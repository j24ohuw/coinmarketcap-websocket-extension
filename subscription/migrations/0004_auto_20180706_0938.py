# Generated by Django 2.0.6 on 2018-07-06 09:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subscription', '0003_auto_20180706_0936'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='subscription',
            unique_together={('owner', 'coin')},
        ),
    ]
