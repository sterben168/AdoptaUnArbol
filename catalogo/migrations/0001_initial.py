# Generated by Django 2.2.5 on 2019-11-12 21:04

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Arbol',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID único para este arbol en todo el catalogo', primary_key=True, serialize=False)),
                ('especie', models.CharField(max_length=200)),
                ('persona', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogo.Persona')),
            ],
        ),
    ]
