from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
    
 #CharField(max_length, min_length, allow_blank, trim_whitespace)
 #IntegerField()
 #FloatField()
 #BooleanField()
 #EmailField()
 #NullBooleanField() bool and None both Valid


#Arguments 
#label, validators, error_message, required, initial, default, input_type, placeholder etc