# Generated by Django 4.2.5 on 2023-09-11 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0004_aluno_celular'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='foto',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
