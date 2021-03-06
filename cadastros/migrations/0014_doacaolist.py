# Generated by Django 3.2.8 on 2021-11-16 19:31

from django.db import migrations, models
import django.db.models.deletion
import django.views.generic.list


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0013_alter_doadores_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoacaoList',
            fields=[
                ('doacao_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='cadastros.doacao')),
                ('doadores_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cadastros.doadores')),
            ],
            bases=(django.views.generic.list.ListView, 'cadastros.doadores', 'cadastros.doacao'),
        ),
    ]
