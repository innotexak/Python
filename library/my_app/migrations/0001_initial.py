# Generated by Django 3.0.6 on 2020-10-05 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autho', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=500)),
                ('image', models.ImageField(upload_to='static')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
