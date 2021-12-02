from django.db import models

# Create your models here.

class data(models.Model):
    date = models.DateField(auto_now_add=True,null=True)
    cm = models.IntegerField(default=0)
    inch = models.IntegerField(default=0)
    time = models.CharField(max_length=99999999,default=' ')
    sensorDate = models.CharField(max_length=99999999,default=' ')
    firstLevel = models.IntegerField(default=0)
    secondLevel = models.IntegerField(default=0)
    thirdLevel = models.IntegerField(default=0)
    arduinoid = models.CharField(max_length=99999999999,default=' ')
   
    def __unicode__(self):
        return "%s" % (self.sensorDate)