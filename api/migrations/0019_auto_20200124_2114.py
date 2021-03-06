# Generated by Django 3.0.1 on 2020-01-24 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20200124_2048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscripcion',
            name='programa',
        ),
        migrations.RemoveField(
            model_name='programa',
            name='precio',
        ),
        migrations.AddField(
            model_name='inscripcion',
            name='nivel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Nivel'),
        ),
        migrations.AddField(
            model_name='nivel',
            name='precio',
            field=models.PositiveSmallIntegerField(default=2000),
            preserve_default=False,
        ),
    ]
