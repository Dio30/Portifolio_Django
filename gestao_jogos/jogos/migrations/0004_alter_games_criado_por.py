# Generated by Django 4.0.4 on 2022-05-30 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('jogos', '0003_alter_games_criado_por'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.cliente'),
        ),
    ]
