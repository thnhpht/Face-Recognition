# Generated by Django 4.1.5 on 2023-03-06 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendances', '0006_alter_user_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
