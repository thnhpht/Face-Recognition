# Generated by Django 4.1.5 on 2023-03-06 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendances', '0003_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(upload_to='static/users/images'),
        ),
    ]
