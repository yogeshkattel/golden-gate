# Generated by Django 3.2.4 on 2021-06-26 09:34

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_slug_blog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
