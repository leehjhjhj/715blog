# Generated by Django 4.0.6 on 2022-07-14 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author_name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
