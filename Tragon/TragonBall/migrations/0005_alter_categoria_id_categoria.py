# Generated by Django 4.0 on 2022-10-25 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TragonBall', '0004_alter_categoria_id_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='id_categoria',
            field=models.AutoField(db_column='ID_Categoria', primary_key=True, serialize=False),
        ),
    ]
