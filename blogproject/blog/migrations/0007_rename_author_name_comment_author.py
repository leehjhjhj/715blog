# Generated by Django 4.0.6 on 2022-07-14 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_comment_author_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author_name',
            new_name='author',
        ),
    ]
