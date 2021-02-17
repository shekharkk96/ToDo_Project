from django.db import models

# Create your models here.
class List(models.Model):
    title = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)
    #created = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        dt=str(self.date)
        tm=str(self.time)
        return str(self.title + " | "+dt+" | "+tm)
