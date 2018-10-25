from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class fooditem(models.Model):
    BREAKFAST = 'BREAKFAST'
    LUNCH = 'LUNCH'
    DINNER = 'DINNER'
    TIMING_CHOICES = (
        (BREAKFAST, 'BREAKFAST'),
        (LUNCH, 'LUNCH'),
        (DINNER, 'DINNER')
    )
    MONDAY = 'MONDAY'
    TUESDAY = 'TUESDAY'
    WEDNESDAY = 'WEDNESDAY'
    THURSDAY = 'THURSDAY'
    FRIDAY = 'FRIDAY'
    SATURDAY = 'SATURDAY'
    SUNDAY  ='SUNDAY'

    WEEK_DAYS = (
        (MONDAY , 'MONDAY'),
        (TUESDAY , 'TUESDAY'),
        (WEDNESDAY , 'WEDNESDAY'),
        (THURSDAY, 'THURSDAY'),
        (FRIDAY , 'FRIDAY'),
        (SATURDAY, 'SATURDAY'),
        (SUNDAY , 'SUNDAY')
    )

    item_name = models.CharField(max_length=250,null=False)
    time = models.CharField(max_length=250,null=False,choices=TIMING_CHOICES,default=None)
    day = models.CharField(max_length=25,null=False,choices=WEEK_DAYS,default=None)

    def __str__(self):
        return self.item_name

