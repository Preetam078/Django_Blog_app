from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

#//TODO: geting all the values / single value ......(class based)


@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
    def get(self, request, *args, **kwargs):
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


    def post(self, request, *args, **kwargs):
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
    

    def put(self, request, *args, **kwargs):
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
    

    def delete(self, request, *args, **kwargs):
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

