# Generated by Django 4.2 on 2024-01-28 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_alter_review_review_desp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.FloatField(max_length=255),
        ),
    ]