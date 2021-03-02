from .models import Email, Contact, Student
from rest_framework import serializers

class EmailSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Email
        fields = ['vnu_email', 'other_email']

class ContactSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Contact
        fields = ['contact_name', 'contact_addr']

class StudentSerializer(serializers.ModelSerializer):
    email = EmailSerializer(read_only=True)
    contacts = ContactSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = [field.name for field in model._meta.fields if field.name ] + ['email','contacts']
        # extra_kwargs = {'created_by': {'read_only': True}}