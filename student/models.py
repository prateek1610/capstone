from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

class Student(models.Model):
    Computer_Science = 'CS'
    Electrical = 'EE'
    Mechanical = 'ME'
    Civil = 'CE'
    Electronics = 'ECE'
    BRANCH_CHOICES = (
        (Computer_Science, 'COMPUTER SCIENCE'),
        (Electrical, 'ELECTRICAL'),
        (Electronics, 'ELECTRONICS'),
        (Civil, 'CIVIL'),
        (Mechanical, 'MECHANICAL'),
    )
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    roll_no = models.IntegerField(unique=True)
    s_name = models.CharField(max_length=100,null=False)
    s_year = models.CharField(max_length=10,null=False)
    s_branch = models.CharField(max_length=20,null=False,choices=BRANCH_CHOICES,default=None)

    def __str__(self):
        return self.user.username


class Holiday(models.Model):
    TIMINGS = (
        ('BREAKFAST','Breakfast'),
        ('LUNCH','Lunch'),
        ('DINNER','Dinner')
    )

    roll_no = models.ForeignKey(Student)
    timing = models.CharField(max_length=20,null=False,choices=TIMINGS,default=None)
    from_date = models.DateTimeField(null=False)
    to_date = models.DateTimeField(null=False)
    total_fine = models.IntegerField()

    def __str__(self):
        return self.timing