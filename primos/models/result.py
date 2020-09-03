from django.db import models


class Result(models.Model):
    """ Class that defines attributes for a result of a request """
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=8, null=False)
    range = models.IntegerField(null=False)
    result = models.CharField(max_length=10000, null=False)
