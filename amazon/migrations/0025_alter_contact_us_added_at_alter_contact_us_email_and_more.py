# Generated by Django 5.0.1 on 2024-02-10 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon', '0024_contact_us_added_at_recipes_opinion_added_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_us',
            name='added_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='message',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='name',
            field=models.CharField(max_length=70),
        ),
    ]
