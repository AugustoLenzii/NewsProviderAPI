# Generated by Django 3.2.6 on 2021-08-30 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_author_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='picture',
            field=models.ImageField(default='blank', upload_to=''),
        ),
    ]
