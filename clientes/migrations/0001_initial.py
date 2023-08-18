from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomecompleto', models.CharField(max_length=150, verbose_name='Nome Completo')),
                ('nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('sexo', models.CharField(choices=[('Feminino', 'Feminino'), ('Masculino', 'Masculino'), ('Outros', 'Outros')], max_length=9, verbose_name='Sexo')),
                ('whatsapp', models.CharField(max_length=15, verbose_name='Whatsapp')),
                ('endereco', models.CharField(max_length=150, verbose_name='Endereço')),
                ('cidade', models.CharField(max_length=30, verbose_name='Cidade')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
        ),
    ]
