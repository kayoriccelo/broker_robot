from django.db import models

from data.config.soros.choices import C_STATUS_SOROS, STATUS_SOROS_ACTIVE


class Soros(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    multiplier = models.IntegerField()
    status = models.IntegerField(choices=C_STATUS_SOROS, default=STATUS_SOROS_ACTIVE, null=True, blank=True)

    class Meta:
        verbose_name = u'Soros'
        verbose_name_plural = u'Soros'
        db_table = 'soros'

    def __str__(self) -> str:
        return f'Multiplier: {self.multiplier}'
