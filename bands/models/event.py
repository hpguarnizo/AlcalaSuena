from django.db import models

from bands.models import Band, Venue


class Event(models.Model):
    band = models.ForeignKey(Band, related_name="band")
    venue = models.ForeignKey(Venue, related_name="venue")
    day = models.DateField(null=False)
    time = models.TimeField(null=False)

    class Meta:
        verbose_name = 'Concierto'
        verbose_name_plural = 'Conciertos'
        ordering = ['day', 'time']

    def __unicode__(self):
        return self.band.name + ' - ' + str(self.day)