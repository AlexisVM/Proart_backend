# Generated by Django 3.0.1 on 2020-01-21 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200118_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='nivel',
            name='clase_derecho',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parcialidades', models.PositiveSmallIntegerField(choices=[('1', 'Una exhibición '), ('3', 'Tres pagos')])),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Persona')),
                ('programa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Programa')),
            ],
        ),
        migrations.CreateModel(
            name='Comprobante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivo', models.FileField(upload_to='comprobantes')),
                ('fecha_de_subida', models.DateField(blank=True, null=True)),
                ('fecha_limite', models.DateField(blank=True, null=True)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=5)),
                ('comprobante', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Inscripcion')),
            ],
        ),
    ]
