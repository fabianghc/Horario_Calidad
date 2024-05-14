# Generated by Django 5.0.5 on 2024-05-07 12:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('modulo_docente', '0001_initial'),
        ('modulo_horario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='disponibilidad_docente',
            name='FKdiasemana',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_horario.dia_semana'),
        ),
        migrations.AddField(
            model_name='docente',
            name='FKdepartamentoacademico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_docente.departamento_academico'),
        ),
        migrations.AddField(
            model_name='disponibilidad_docente',
            name='FKdocente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_docente.docente'),
        ),
        migrations.AddField(
            model_name='docente',
            name='FKtipocontrato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_docente.tipo_contrato'),
        ),
    ]
