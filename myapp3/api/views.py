from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

#//TODO: geting all the values / single value ......

@csrf_exempt
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
    
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        serializer = StudentSerializer(data = pythonData)
        if serializer.is_valid():
            serializer.save()
            res = {"message":"success"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    

    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        uniqueId = pythonData.get('id')
        stu = Student.objects.get(id=uniqueId)
        serializer = StudentSerializer(stu, data=pythonData, partial = True)

        if serializer.is_valid():
            serializer.save()
            res = {"message":"update successful"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")
        
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    
    if request.method == 'DELETE':
        try:
            json_data = request.body
            stream = io.BytesIO(json_data)
            pythondata = JSONParser().parse(stream)
            uniqueId = pythondata.get('id')
            stu = Student.objects.get(id=uniqueId)
            stu.delete()
            res = {'message':"data deleted successfully"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        except:
            res = {'message':"data not deleted"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')



    

#//TODO: geting all the values / single value ......(alternative way)
def student_apiParams(request, id):
    if request.method == 'GET':
        uniqueId = id
        stu = Student.objects.get(id = uniqueId)
        serializer = StudentSerializer(stu)
        return JsonResponse(serializer.data,safe=False)


#//TODO: create student data and store in the DB 
