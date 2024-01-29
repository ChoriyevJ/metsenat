from django.db import models


class BaseModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    tel_number = models.CharField(max_length=13)
    actions = models.BooleanField(default=False)

    class Meta:
        abstract = True
