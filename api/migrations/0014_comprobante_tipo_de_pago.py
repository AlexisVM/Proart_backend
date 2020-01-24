# Generated by Django 3.0.1 on 2020-01-24 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20200123_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='comprobante',
            name='tipo_de_pago',
            field=models.CharField(choices=[('D', 'Depósito'), ('T', 'Transferencia'), ('E', 'Efectivo')], default='D', max_length=3),
        ),
    ]