# Generated by Django 5.0.1 on 2024-02-05 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon', '0012_alter_blogrecipes_active_alter_blogrecipes_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogrecipes',
            name='publisher',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
