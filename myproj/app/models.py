from django.db import models

class Company(models.Model):
    IT = 'IT'
    NON_IT = 'Non-IT'
    NGOS = 'NGOs'
    INGOS = 'INGOs'

    COMPANY_TYPE_CHOICES = [
        (IT, 'IT'),
        (NON_IT, 'Non-IT'),
        (NGOS, 'NGOs'),
        (INGOS, 'INGOs'),
    ]

    company_id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=50)
    location = models.TextField(max_length=50)
    about = models.TextField(max_length=250)
    type = models.CharField(max_length=20, choices=COMPANY_TYPE_CHOICES)
    active = models.BooleanField(default=True)
    added_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

#employe models made with one to many relationship

class Employees(models.Model):

    manager = 'manager'
    boardmember = 'board-member'
    softwareeng = 'software-engineer'
    other = 'other'
    Employee_TYPE_CHOICES = [
        (manager, 'manager'),
        (boardmember, 'board-member'),
        (softwareeng, 'software-engineer'),
        (other, 'other'),
    ]


    name = models.CharField(max_length=200)
    email = models.CharField(max_length=40)
    address=models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=50)
    positions =  models.CharField(max_length=20, choices=Employee_TYPE_CHOICES)

    company = models.ForeignKey(Company,on_delete=models.CASCADE)       #linkage between company and employee
