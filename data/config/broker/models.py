from django.db import models


class Broker(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=True, null=True, blank=True)

    class Meta:
        verbose_name = u'Broker'
        verbose_name_plural = u'Broker'
        db_table = 'broker'

    def __str__(self) -> str:
        return self.description
