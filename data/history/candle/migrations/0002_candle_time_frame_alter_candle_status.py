# Generated by Django 4.2 on 2023-12-24 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candle',
            name='time_frame',
            field=models.IntegerField(choices=[(1, 'M1'), (2, 'M5'), (3, 'M15')], default=1),
        ),
        migrations.AlterField(
            model_name='candle',
            name='status',
            field=models.IntegerField(choices=[(1, 'Active'), (2, 'Inactive')], default=1),
        ),
    ]
