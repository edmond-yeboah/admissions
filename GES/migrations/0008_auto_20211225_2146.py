# Generated by Django 3.1.7 on 2021-12-25 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GES', '0007_auto_20211225_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='degree_programs',
            name='readmore',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='diploma_programs',
            name='readmore',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='hnd_programs',
            name='readmore',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]