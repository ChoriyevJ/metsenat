from django.db import models
from api.utils.models import BaseModel


class Sponsor(BaseModel):

    class Status(models.TextChoices):
        ALL = 'ALL', 'Barchasi'
        NEW = 'NEW', 'Yangi',
        MOD = 'MOD', 'Modernizatsiyada',
        APP = 'APP', 'Tasdiqlangan',
        CAN = 'CAN', 'Bekor qilingan'

    class PersonType(models.TextChoices):
        INDIVIDUAL = 'IND', 'Jismoniy'
        LEGAL = 'LEG', 'Yuridik'

    class PaymentType(models.TextChoices):
        EXP1 = 'EXP1', 'Example1'
        EXP2 = 'EXP2', 'Example2'

    sponsorship_sum = models.CharField(max_length=20)
    spent_sum = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=3,
                              choices=Status.choices,
                              default=Status.ALL)
    person_type = models.CharField(max_length=3,
                                   choices=PersonType.choices,
                                   default=PersonType.INDIVIDUAL)
    payment_type = models.CharField(max_length=4,
                                    choices=PaymentType.choices,
                                    default=PaymentType.EXP1)
    organization = models.CharField(max_length=200, blank=True, default=None, null=True)

    class Meta:
        ordering = ['last_name']
        indexes = [
            models.Index(fields=['last_name'])
        ]

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'

    def __repr__(self):
        return f'Sponsor(pk={self.pk}, full_name="{self.last_name} {self.first_name} {self.middle_name}")'


class HTI(models.Model):

    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class SponsorForStudent(models.Model):
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE, related_name='sponsors')
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='students')
    allocated_sum = models.CharField(max_length=20, default="0")

    def __str__(self):
        return f'{self.pk}'


class Student(BaseModel):

    class StudentType(models.TextChoices):
        GRAD = 'GR', 'Bakalavr'
        MAGS = 'MG', 'Magistr'

    student_type = models.CharField(max_length=2,
                                    choices=StudentType.choices)
    hti = models.ForeignKey(HTI, on_delete=models.CASCADE, related_name='htis')
    allocated_sum = models.CharField(max_length=20, default='0')
    contract_amount = models.CharField(max_length=20)

    class Meta:
        ordering = ['last_name']
        indexes = [
            models.Index(fields=['last_name'])
        ]

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'

    def __repr__(self):
        return f'Student(pk={self.pk}, full_name="{self.last_name} {self.first_name} {self.middle_name}")'


