# Generated by Django 4.1.3 on 2022-11-17 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_music_list', '0003_alter_song_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='durations',
            field=models.CharField(max_length=55),
        ),
    ]
