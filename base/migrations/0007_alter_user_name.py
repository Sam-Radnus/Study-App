# Generated by Django 4.0.4 on 2022-06-01 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_room_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(db_index=True, max_length=255, null=True, unique=True),
        ),
    ]
