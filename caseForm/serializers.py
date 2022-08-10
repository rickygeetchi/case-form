from rest_framework import serializers
from caseForm.models import CaseForm

class CaseFormSerializers(serializers.ModelSerializer):
    class Meta:
        model=CaseForm

        fields=('CaseId','FirstName','LastName','TicketNumber','DriverLicense')