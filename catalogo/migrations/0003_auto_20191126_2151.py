# Generated by Django 2.2.5 on 2019-11-26 21:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_auto_20191126_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arbol',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='ID único para este arbol en todo el catalogo', primary_key=True, serialize=False),
        ),
    ]
