# Generated by Django 4.0.4 on 2022-04-29 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indexers', '0002_alter_githubindexer_current_page'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='githubindexer',
            options={'verbose_name': 'Github Indexer', 'verbose_name_plural': 'Github Indexer'},
        ),
    ]
