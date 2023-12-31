# Generated by Django 4.2.4 on 2023-08-16 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_login', '0002_remove_cadastro_last_login_remove_cadastro_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='cadastro',
            name='password',
            field=models.CharField(default=1, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='email_usuario',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='nome_usuario',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='senha',
            field=models.CharField(default='senha123', max_length=16),
        ),
    ]
