# Generated by Django 5.0.1 on 2024-02-09 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amazon', '0017_alter_recipes_populat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipes',
            old_name='populat',
            new_name='popular',
        ),
    ]
