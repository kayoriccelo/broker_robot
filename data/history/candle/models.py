from datetime import datetime

from django.db import models

from data.history.candle.choices import (
    C_STATUS_CANDLE, C_TIME_FRAME_CANDLE, STATUS_CANDLE_ACTIVE, TIME_FRAME_CANDLE_M1
)


class Candle(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    identity_broker = models.IntegerField()
    date_from = models.IntegerField()
    date_at = models.IntegerField()
    date_to = models.IntegerField()
    value_open = models.DecimalField(max_digits=19, decimal_places=8, default=0)
    value_close = models.DecimalField(max_digits=19, decimal_places=8, default=0)
    value_max = models.DecimalField(max_digits=19, decimal_places=8, default=0)
    value_min = models.DecimalField(max_digits=19, decimal_places=8, default=0)
    volume = models.DecimalField(max_digits=19, decimal_places=8, default=0)
    time_frame = models.IntegerField(choices=C_TIME_FRAME_CANDLE, default=TIME_FRAME_CANDLE_M1)
    status = models.IntegerField(choices=C_STATUS_CANDLE, default=STATUS_CANDLE_ACTIVE)
    active = models.ForeignKey('active.Active', related_name='candles', on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'Candle'
        verbose_name_plural = u'Candles'
        db_table = 'candle'

    def __str__(self) -> str:
        return f'{self.date_from_display} - {self.color}'

    @property
    def date_from_display(self):
        return datetime.fromtimestamp(self.date_from).strftime("%d/%m/%Y")
    
    @property
    def time_from_display(self):
        return datetime.fromtimestamp(self.date_from).strftime("%H:%M")

    @property
    def color(self):
        return 'green' if self.open < self.close else 'red' if self.open > self.close else 'doji'
