from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

#//TODO: geting all the values / single value ......
def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        uniqueId = pythondata.get('id',None)

        if uniqueId is not None:
            stu = Student.objects.get(id = uniqueId)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type="application/json")
        
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type="application/json")
    

#//TODO: geting all the values / single value ......(alternative way)
def student_apiParams(request, id):
    if request.method == 'GET':
        uniqueId = id
        stu = Student.objects.get(id = uniqueId)
        serializer = StudentSerializer(stu)
        return JsonResponse(serializer.data,safe=False)


