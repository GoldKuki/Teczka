# Generated by Django 3.2 on 2021-05-04 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_alter_video_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='video',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='videos.Tags'),
        ),
    ]
