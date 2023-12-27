from django.db import models

from data.config.strategy.choices import C_STATUS_STRATEGY, STATUS_STRATEGY_ACTIVE


class Strategy(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=200)
    status = models.IntegerField(choices=C_STATUS_STRATEGY, default=STATUS_STRATEGY_ACTIVE, null=True, blank=True)
    
    account = models.ForeignKey('account.Account', related_name='strategies', on_delete=models.CASCADE)
    cycles = models.ManyToManyField('cycle.Cycle', related_name='strategies', blank=True)
    
    class Meta:
        verbose_name = u'Strategy'
        verbose_name_plural = u'Strategies'
        db_table = 'strategy'

    def __str__(self) -> str:
        return self.description
