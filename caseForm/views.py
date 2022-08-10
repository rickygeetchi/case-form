import re
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from caseForm.models import CaseForm
from caseForm.serializers import CaseFormSerializers
# Create your views here.

@csrf_exempt
def lawyerAPI(request,id=0):
    if request.method =='GET':
        caseform = CaseForm.objects.all()
        caseform_serializer=CaseFormSerializers(caseform,many=True)
        return JsonResponse(caseform_serializer.data,safe=False)
    elif request.method =='POST':
        caseform_data=JSONParser().parse(request)
        caseform_serializer=CaseFormSerializers(data=caseform_data)
        if caseform_serializer.is_valid():
            caseform_serializer.save()
            return JsonResponse("Added Succesfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method == 'PUT':
        caseform_data=JSONParser().parse(request)
        caseform=CaseForm.objects.get(CaseId=caseform_data['CaseId'])
        caseform_serializer=CaseFormSerializers(caseform,data=caseform_data)
        if caseform_serializer.is_valid():
            caseform_serializer.save()
            return JsonResponse("Update Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method =='DELETE':
        caseform=CaseForm.objects.get(CaseId=id)
        caseform.delete()
        return JsonResponse("Deleted Succesfully",safe=False)