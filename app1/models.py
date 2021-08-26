from django.db import models

class Touroku(models.Model):
    name = models.CharField(max_length=30)
    gender = models.BooleanField()
    age = models.IntegerField(default = 0)

    def __str__(self):
        return '<ID:'+str(self.id)+'>  名前:'+self.name+' ('+str(self.age)+'歳)'