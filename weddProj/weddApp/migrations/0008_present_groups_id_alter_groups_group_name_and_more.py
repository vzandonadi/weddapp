# Generated by Django 4.1 on 2022-09-24 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weddApp', '0007_alter_guests_is_confirmed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Present',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='groups',
            name='group_name',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AddField(
            model_name='groups',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='guests',
            name='is_confirmed',
            field=models.CharField(choices=[('O', 'N/I'), ('Y', 'SIM'), ('N', 'NÃO')], default='O', max_length=1),
        ),
    ]
