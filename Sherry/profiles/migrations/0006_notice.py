# Generated by Django 3.2 on 2021-05-11 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_rename_backgraund_profile_background'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('reciver', models.ManyToManyField(to='profiles.Profile')),
            ],
        ),
    ]
