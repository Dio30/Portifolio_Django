# Generated by Django 4.0.4 on 2022-05-23 14:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jogos', '0003_alter_games_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='games',
            options={'ordering': ['nome_do_jogo'], 'verbose_name_plural': 'Jogos'},
        ),
        migrations.AddField(
            model_name='games',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]