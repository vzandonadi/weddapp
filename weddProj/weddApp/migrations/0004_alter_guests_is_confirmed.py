# Generated by Django 4.1 on 2022-09-24 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weddApp', '0003_alter_guests_is_confirmed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guests',
            name='is_confirmed',
            field=models.BooleanField(choices=[('Y', 'SIM'), ('N', 'NÃO'), ('', 'N/I')], default='N/I'),
        ),
    ]
