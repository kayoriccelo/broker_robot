# Generated by Django 4.2 on 2023-12-26 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Soros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('multiplier', models.IntegerField()),
                ('status', models.IntegerField(blank=True, choices=[(1, 'Active'), (2, 'Inactive')], default=1, null=True)),
            ],
            options={
                'verbose_name': 'Soros',
                'verbose_name_plural': 'Soros',
                'db_table': 'soros',
            },
        ),
    ]
