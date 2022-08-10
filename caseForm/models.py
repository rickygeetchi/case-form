from django.db import models

# Create your models here.

class CaseForm(models.Model):
    CaseId = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=500)
    LastName = models.CharField(max_length=500)
    TicketNumber = models.CharField(max_length=500)
    DriverLicense = models.CharField(max_length=500)
