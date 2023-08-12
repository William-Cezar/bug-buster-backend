# Generated by Django 4.1.7 on 2023-08-07 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('Aberto', 'Aberto'), ('Em análise', 'Em análise'), ('Resolvido', 'Resolvido'), ('Fechado', 'Fechado')], max_length=50)),
                ('priority', models.CharField(choices=[('Baixa', 'Baixa'), ('Normal', 'Normal'), ('Alta', 'Alta')], max_length=50)),
                ('category', models.CharField(choices=[('Front-end', 'Front-end'), ('Back-end', 'Back-end'), ('Banco de Dados', 'Banco de Dados')], max_length=50)),
            ],
        ),
    ]