# Generated by Django 3.2.6 on 2021-08-26 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Touroku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=30)),
                ('breakfast', models.BooleanField()),
                ('lunch', models.BooleanField()),
                ('dinner', models.BooleanField()),
                ('eatout', models.BooleanField()),
                ('drinking', models.BooleanField()),
                ('workout', models.BooleanField()),
                ('stretch', models.BooleanField()),
                ('studying', models.BooleanField()),
                ('awaketime', models.TimeField()),
                ('asleeptime', models.TimeField()),
                ('kenkobody', models.CharField(max_length=30)),
                ('workcond', models.CharField(max_length=30)),
            ],
        ),
    ]
