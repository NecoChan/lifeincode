# Generated by Django 2.2.4 on 2019-12-16 14:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('syte', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='В написании', max_length=10, verbose_name='Статус'),
        ),
    ]
