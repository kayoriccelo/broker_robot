from django.db import models

from data.config.broker.choices import C_STATUS_BROKER, STATUS_BROKER_ACTIVE


class Broker(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=200)
    status = models.IntegerField(choices=C_STATUS_BROKER, default=STATUS_BROKER_ACTIVE, null=True, blank=True)
    active = models.ManyToManyField('active.Active', related_name='brokers', blank=True)

    class Meta:
        verbose_name = u'Broker'
        verbose_name_plural = u'Broker'
        db_table = 'broker'

    def __str__(self) -> str:
        return self.description
