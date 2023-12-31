# Generated by Django 4.2.1 on 2023-05-12 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chatbot', '0002_remove_besttouristattractions_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='besttouristattractions',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='campingsites',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cities',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='conservationforests',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='factories',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='farms',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='gardens',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='hikingareas',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='hotels',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='lakes_reservors',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='mountainpeaks',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='nationalparks',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='parks',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='religious_places',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='waterfalls',
            name='description',
            field=models.CharField(max_length=255),
        ),
    ]
