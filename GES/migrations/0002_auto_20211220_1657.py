# Generated by Django 3.1.7 on 2021-12-20 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GES', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='degree_programs',
            name='degree_schools',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='GES.school'),
        ),
        migrations.AddField(
            model_name='diploma_programs',
            name='diploma_schools',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='GES.school'),
        ),
        migrations.AddField(
            model_name='hnd_programs',
            name='hnd_schools',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='GES.school'),
        ),
    ]