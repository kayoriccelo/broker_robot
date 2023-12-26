from django.db import models

from data.config.strategy_candle.choices import C_COLOR_STRATEGY_CANDLE, C_STATUS_STRATEGY_CANDLE, STATUS_STRATEGY_CANDLE_ACTIVE


class StrategyCandle(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    sequence = models.IntegerField(default=0, null=True, blank=True)
    color = models.IntegerField(choices=C_COLOR_STRATEGY_CANDLE)
    compare = models.BooleanField(default=False, null=True, blank=True)
    conditional = models.BooleanField(default=False, null=True, blank=True)
    status = models.IntegerField(choices=C_STATUS_STRATEGY_CANDLE, default=STATUS_STRATEGY_CANDLE_ACTIVE, null=True, blank=True)

    strategy = models.ForeignKey('strategy.Strategy', related_name='strategies_candles', on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'Strategy Candle'
        verbose_name_plural = u'Strategies Candles'
        db_table = 'strategy_candle'

    def __str__(self) -> str:
        return f'{self.sequence} - {self.get_color_display()} - Compare: {self.compare} - Conditional: {self.conditional}'
