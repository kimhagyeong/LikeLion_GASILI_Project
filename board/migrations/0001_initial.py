# Generated by Django 2.2.3 on 2019-08-19 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(max_length=20)),
                ('body', models.TextField()),
                ('product_price', models.PositiveIntegerField(blank=True, default=0)),
                ('order_price', models.PositiveIntegerField(default=0)),
                ('state', models.CharField(max_length=15)),
                ('userId', models.IntegerField()),
                ('userName', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('image1', models.ImageField(blank=True, upload_to='images/')),
                ('image2', models.ImageField(blank=True, upload_to='images/')),
                ('image3', models.ImageField(blank=True, upload_to='images/')),
                ('image4', models.ImageField(blank=True, upload_to='images/')),
                ('image5', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.IntegerField()),
                ('userId', models.IntegerField()),
                ('author', models.CharField(max_length=15)),
                ('text', models.TextField()),
                ('price', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('approved_comment', models.BooleanField(default=False)),
            ],
        ),
    ]
