# Generated by Django 2.2.4 on 2019-12-16 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syte', '0002_auto_20191216_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d', verbose_name='Изображение'),
        ),
    ]
