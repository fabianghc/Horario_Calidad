# Generated by Django 5.0.4 on 2024-05-01 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_curso', '0006_alter_curso_options_alter_escuela_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan_estudio',
            name='plan_estado',
            field=models.BooleanField(default=True),
        ),
    ]
