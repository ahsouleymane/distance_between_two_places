# Generated by Django 4.1.1 on 2022-09-29 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('near', '0002_mesure'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Mesure',
        ),
        migrations.AlterField(
            model_name='coordonnees',
            name='latitude',
            field=models.DecimalField(decimal_places=20, max_digits=20),
        ),
        migrations.AlterField(
            model_name='coordonnees',
            name='longitude',
            field=models.DecimalField(decimal_places=20, max_digits=20),
        ),
    ]
