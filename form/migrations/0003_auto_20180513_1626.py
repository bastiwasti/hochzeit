# Generated by Django 2.0.5 on 2018-05-13 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_auto_20180512_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='eintrag',
            name='Email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='eintrag',
            name='Anmeldung',
            field=models.CharField(choices=[('1', 'Ja'), ('2', 'Nein'), ('3', 'Noch nicht entschieden')], max_length=2),
        ),
        migrations.AlterField(
            model_name='eintrag',
            name='Essen',
            field=models.CharField(choices=[('1', 'Fleisch'), ('2', 'Fisch'), ('3', 'Vegetarisch')], max_length=2),
        ),
    ]
