from django.db import models

from data.config.martingale.choices import C_STATUS_MARTINGALE, STATUS_MARTINGALE_ACTIVE


class Martingale(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    multiplier = models.IntegerField()
    status = models.IntegerField(choices=C_STATUS_MARTINGALE, default=STATUS_MARTINGALE_ACTIVE, null=True, blank=True)

    class Meta:
        verbose_name = u'Martingale'
        verbose_name_plural = u'Martingale'
        db_table = 'martingale'
