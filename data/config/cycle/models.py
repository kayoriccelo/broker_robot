from django.db import models

from data.config.cycle.choices import C_STATUS_CYCLE, STATUS_CYCLE_ACTIVE


class Cycle(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    sequence = models.IntegerField(default=0, null=True, blank=True)
    status = models.IntegerField(choices=C_STATUS_CYCLE, default=STATUS_CYCLE_ACTIVE, null=True, blank=True)

    martingale = models.ForeignKey('martingale.Martingale', related_name='cycles', on_delete=models.CASCADE)
    soros = models.ForeignKey('soros.Soros', related_name='cycles', on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'Cycle'
        verbose_name_plural = u'Cycle'
        db_table = 'cycle'

    def __str__(self) -> str:
        return self.sequence
