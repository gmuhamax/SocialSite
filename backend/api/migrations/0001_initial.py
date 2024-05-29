# Generated by Django 5.0.4 on 2024-05-24 11:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preview', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('dislike', models.IntegerField()),
                ('like', models.IntegerField()),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=200)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.user')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.post')),
            ],
        ),
    ]