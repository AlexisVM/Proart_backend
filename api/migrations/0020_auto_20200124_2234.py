# Generated by Django 3.0.1 on 2020-01-24 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20200124_2114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bloque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('inicio', models.TimeField()),
                ('final', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Paquete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.TextField(max_length=30)),
                ('semanas', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Semana',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_final', models.DateField()),
            ],
        ),
        migrations.RenameField(
            model_name='programa',
            old_name='dirgido',
            new_name='dirigido',
        ),
        migrations.RemoveField(
            model_name='grupo',
            name='fecha_final',
        ),
        migrations.RemoveField(
            model_name='grupo',
            name='fecha_inicio',
        ),
        migrations.RemoveField(
            model_name='inscripcion',
            name='grupo',
        ),
        migrations.AddField(
            model_name='inscripcion',
            name='grupos',
            field=models.ManyToManyField(to='api.Grupo'),
        ),
        migrations.AddField(
            model_name='inscripcion',
            name='programa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Programa'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='bloque',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Bloque'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='semana',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='grupos', to='api.Semana'),
        ),
        migrations.AddField(
            model_name='inscripcion',
            name='paquete',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Paquete'),
        ),
        migrations.AddField(
            model_name='programa',
            name='bloques',
            field=models.ManyToManyField(to='api.Bloque'),
        ),
    ]
