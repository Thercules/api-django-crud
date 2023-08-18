from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='ativo',
            field=models.BooleanField(default=True, verbose_name='Ativo'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='bairro',
            field=models.CharField(default='', max_length=100, verbose_name='Bairro'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='cep',
            field=models.CharField(default='', max_length=10, verbose_name='CEP'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=14, unique=True, verbose_name='CPF'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='estado',
            field=models.CharField(default='', max_length=50, verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='logradouro',
            field=models.CharField(default='', max_length=255, verbose_name='Logradouro'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='numero',
            field=models.CharField(default='', max_length=10, verbose_name='Número'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cidade',
            field=models.CharField(default='', max_length=100, verbose_name='Cidade'),
        ),
    ]
