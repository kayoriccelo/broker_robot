# Generated by Django 4.2 on 2023-12-26 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cycle', '0001_initial'),
        ('active', '0001_initial'),
        ('broker', '0002_broker_status_remove_broker_active_broker_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=200)),
                ('status', models.IntegerField(blank=True, choices=[(1, 'Active'), (2, 'Inactive')], default=1, null=True)),
                ('active', models.ManyToManyField(related_name='managements', to='active.active')),
                ('broker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='managements', to='broker.broker')),
                ('cycles', models.ManyToManyField(blank=True, related_name='managements', to='cycle.cycle')),
            ],
            options={
                'verbose_name': 'Management',
                'verbose_name_plural': 'Management',
                'db_table': 'management',
            },
        ),
    ]