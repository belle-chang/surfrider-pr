from django.db import models

# Create your models here.
class Beach(models.Model):
    beach_name = models.CharField(max_length=200)
    date_visited = models.DateTimeField('date visited')
    # count = models.IntegerField(default=0)
    def __str__(self):
        return '%s' % (self.beach_name)

class BeachNameID(models.Model):
    beach_name = models.CharField(max_length=200)
    beach_id = models.IntegerField(default=0)
    def __str__(self):
        return '%s %d' % (self.beach_name, self.beach_id)

