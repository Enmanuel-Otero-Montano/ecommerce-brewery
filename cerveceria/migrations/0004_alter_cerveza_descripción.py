# Generated by Django 4.0.4 on 2022-08-27 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cerveceria', '0003_rename_descripcion_cerveza_descripción_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cerveza',
            name='descripción',
            field=models.TextField(),
        ),
    ]
