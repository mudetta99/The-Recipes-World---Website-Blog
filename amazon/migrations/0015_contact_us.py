# Generated by Django 5.0.1 on 2024-02-07 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon', '0014_blogs_alter_recipes_added_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
