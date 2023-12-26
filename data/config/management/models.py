from django.db import models

from data.config.management.choices import C_STATUS_MANAGEMENT, STATUS_MANAGEMENT_ACTIVE


class Management(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=200)
    status = models.IntegerField(choices=C_STATUS_MANAGEMENT, default=STATUS_MANAGEMENT_ACTIVE, null=True, blank=True)
    
    broker = models.ForeignKey('broker.Broker', related_name='managements', on_delete=models.CASCADE)
    active = models.ManyToManyField('active.Active', related_name='managements')
    cycles = models.ManyToManyField('cycle.Cycle', related_name='managements', blank=True)

    class Meta:
        verbose_name = u'Management'
        verbose_name_plural = u'Management'
        db_table = 'management'

    def __str__(self) -> str:
        return self.description
