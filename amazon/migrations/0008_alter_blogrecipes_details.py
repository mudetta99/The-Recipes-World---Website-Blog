# Generated by Django 5.0.1 on 2024-01-30 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon', '0007_alter_blogrecipes_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogrecipes',
            name='details',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
