from django.db import models

class Touroku(models.Model):

    date = models.DateField()
    name = models.CharField(max_length=30)
    breakfast = models.BooleanField()
    lunch = models.BooleanField()
    dinner = models.BooleanField()
    eatout = models.BooleanField()
    drinking = models.BooleanField()
    workout = models.BooleanField()
    stretch = models.BooleanField()
    studying = models.BooleanField()
    awaketime = models.TimeField()
    asleeptime = models.TimeField()
    kenkobody = models.CharField(max_length=30)
    workcond = models.CharField(max_length=30)

    def __str__(self):
        return '<ID:'+str(self.id)+'>  名前:'+self.name