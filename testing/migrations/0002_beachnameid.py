# Generated by Django 2.2 on 2019-06-25 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BeachNameID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beach_name', models.CharField(max_length=200)),
                ('beach_id', models.IntegerField(default=0)),
            ],
        ),
    ]