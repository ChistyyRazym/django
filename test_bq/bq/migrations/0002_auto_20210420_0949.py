# Generated by Django 3.2 on 2021-04-20 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bq', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='test_1',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ip', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('method', models.CharField(max_length=1500)),
                ('url', models.CharField(max_length=1500)),
                ('status_code', models.CharField(max_length=4)),
                ('response_size', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='test',
        ),
    ]
