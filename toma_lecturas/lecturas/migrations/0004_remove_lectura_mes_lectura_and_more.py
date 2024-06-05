# Generated by Django 5.0.3 on 2024-05-09 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecturas', '0003_alter_micromedidor_nuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lectura',
            name='Mes_lectura',
        ),
        migrations.RemoveField(
            model_name='lectura',
            name='registro_consumo',
        ),
        migrations.AddField(
            model_name='lectura',
            name='consumototal',
            field=models.IntegerField(default=0, verbose_name='Consumo total'),
        ),
        migrations.AddField(
            model_name='lectura',
            name='lectura_actual',
            field=models.IntegerField(default=0, verbose_name='Lectura actual'),
        ),
        migrations.AddField(
            model_name='lectura',
            name='lectura_anterior',
            field=models.IntegerField(default=0, verbose_name='Lectura anterior'),
        ),
        migrations.AddField(
            model_name='lectura',
            name='mes_actual',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Mes actual'),
        ),
        migrations.AddField(
            model_name='lectura',
            name='mes_anterior',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Mes anterior'),
        ),
        migrations.AlterField(
            model_name='lectura',
            name='FechaLectura',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Lectura'),
        ),
        migrations.AlterField(
            model_name='lectura',
            name='Observaciones',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='lectura',
            name='estado_micromedidor',
            field=models.CharField(choices=[('estado1', 'Bueno'), ('estado2', 'Malo')], max_length=50, null=True, verbose_name='Estado del micromedidor'),
        ),
        migrations.AlterField(
            model_name='lectura',
            name='tipo_lectura',
            field=models.CharField(choices=[('tipo1', 'Lectura'), ('tipo2', 'Promedio')], max_length=50, null=True, verbose_name='Tipo de lectura'),
        ),
    ]
