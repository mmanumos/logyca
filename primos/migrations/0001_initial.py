# Generated by Django 3.0.8 on 2020-09-03 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=8)),
                ('range', models.IntegerField()),
                ('result', models.CharField(max_length=10000)),
            ],
        ),
    ]