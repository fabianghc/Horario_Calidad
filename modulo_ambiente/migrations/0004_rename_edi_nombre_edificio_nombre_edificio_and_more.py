# Generated by Django 5.0.4 on 2024-04-13 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_ambiente', '0003_rename_fktipoambiente_ambiente_fktipo_ambiente_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='edificio',
            old_name='edi_nombre',
            new_name='nombre_edificio',
        ),
        migrations.RenameField(
            model_name='tipo_ambiente',
            old_name='tipamb_descripcion',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='tipo_ambiente',
            old_name='tipamb_nombre',
            new_name='tipo_de_ambiente',
        ),
    ]
