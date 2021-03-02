from .models import Email, Contact, Student
from rest_framework import serializers


class EmailSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Email
        fields = [field.name for field in model._meta.fields if field.name != 'student']

class ContactSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Email
        fields = [field.name for field in model._meta.fields if field.name != 'student']

class StudentSerializer(serializers.ModelSerializer):
    email = EmailSerializer()
    contacts = ContactSerializer(many=True)

    class Meta:
        model = Email
        fields = [field.name for field in model._meta.fields if field.name ] + ['email' + 'contacts']