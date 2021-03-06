# Generated by Django 3.0.1 on 2020-01-24 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20200124_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupo',
            name='fecha_final',
            field=models.DateField(default='2020-01-01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo',
            name='fecha_inicio',
            field=models.DateField(default='2020-01-01'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='grupo',
            name='maestro',
            field=models.ManyToManyField(related_name='maestros', to='api.Persona'),
        ),
    ]
