# Generated by Django 4.0.4 on 2022-05-18 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nome_do_jogo', models.CharField(max_length=30)),
                ('tipo_de_jogo', models.CharField(max_length=30)),
                ('preço_do_jogo', models.DecimalField(decimal_places=2, max_digits=7)),
                ('descrição_do_jogo', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
