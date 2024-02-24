# Generated by Django 5.0.1 on 2024-01-30 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon', '0005_alter_blogrecipes_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogrecipes',
            name='active',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='blogrecipes',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='blogrecipes',
            name='details',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='blogrecipes',
            name='image',
            field=models.ImageField(null=True, upload_to='photos/blog/%y/%m/%d'),
        ),
    ]
