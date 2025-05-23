# Generated by Django 5.2 on 2025-05-14 22:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0002_alter_institution_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/areas')),
            ],
            options={
                'verbose_name': 'Área',
                'verbose_name_plural': 'Áreas',
            },
        ),
        migrations.AddField(
            model_name='career',
            name='area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='institutions.area'),
        ),
    ]
