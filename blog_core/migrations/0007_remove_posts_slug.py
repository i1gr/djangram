# Generated by Django 4.0.2 on 2022-03-16 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_core', '0006_posts_uniqueid_alter_posts_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='slug',
        ),
    ]
