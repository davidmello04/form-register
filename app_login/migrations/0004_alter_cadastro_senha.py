# Generated by Django 4.2.4 on 2023-08-16 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_login', '0003_cadastro_last_login_cadastro_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='senha',
            field=models.CharField(max_length=16),
        ),
    ]