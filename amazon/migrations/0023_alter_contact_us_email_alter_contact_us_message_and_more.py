# Generated by Django 5.0.1 on 2024-02-10 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon', '0022_alter_recipes_opinion_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_us',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='message',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='name',
            field=models.CharField(max_length=70, null=True),
        ),
    ]