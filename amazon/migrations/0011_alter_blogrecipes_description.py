# Generated by Django 5.0.1 on 2024-01-30 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon', '0010_alter_blogrecipes_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogrecipes',
            name='description',
            field=models.TextField(),
        ),
    ]