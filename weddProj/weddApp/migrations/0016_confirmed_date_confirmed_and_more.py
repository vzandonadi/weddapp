# Generated by Django 4.1 on 2022-10-10 17:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('weddApp', '0015_confirmed_rename_indivdualmsg_individualmsg_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='confirmed',
            name='date_confirmed',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='confirmed',
            name='relationship',
            field=models.CharField(choices=[('SELF', 'Convidado'), ('PARENTS', 'Pais'), ('RELATIVES', 'Familiares'), ('CHILDRENS', 'Filho(a)'), ('FRIENDS', 'Amigo(a)'), ('PARTNER', 'Parceiro(a)/Companheiro(a)')], max_length=10),
        ),
    ]
