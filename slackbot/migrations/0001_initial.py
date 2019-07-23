# Generated by Django 2.2.3 on 2019-07-23 20:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slackuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('last_reminder', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_private_nag', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_public_nag', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.TextField()),
                ('text', models.TextField(max_length=500)),
                ('dt', models.DateTimeField()),
                ('slackuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slackbot.Slackuser')),
            ],
        ),
    ]
