from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)


   #//TODO: it is important to when we have to store data in DB
    def create(self, validate_data):
        return Student.objects.create(**validate_data)
    
    #//TODO: implementing update template....
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)

        instance.save()
        return instance