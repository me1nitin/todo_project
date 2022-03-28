from django.db import models


# Create your models here.
class TodoData(models.Model):
    name = models.CharField(max_length=250)
    priority = models.IntegerField()
    date = models.DateField()
    desc = models.TextField(null=True)

    def __str__(self):
        return self.name
