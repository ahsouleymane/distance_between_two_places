# Generated by Django 4.1.1 on 2022-09-28 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coordonnees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emplacement', models.CharField(max_length=150)),
                ('latitude', models.DecimalField(decimal_places=4, max_digits=20)),
                ('longitude', models.DecimalField(decimal_places=4, max_digits=20)),
            ],
        ),
    ]