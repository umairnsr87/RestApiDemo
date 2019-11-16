from rest_framework import serializers
#from rest_framework import employees
from .models import employee

#making the class now
class employeeSerializer(serializers.ModelSerializer):

    class Meta:
        model=employee
        fields='__all__'