# Generated by Django 3.2 on 2021-05-11 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0014_auto_20210511_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
