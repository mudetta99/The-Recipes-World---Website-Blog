# Generated by Django 5.0.1 on 2024-01-30 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon', '0004_alter_blogrecipes_added_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogrecipes',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
