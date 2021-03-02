from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from server import api

app_name = 'server'

urlpatterns = [
    path('students/', api.student_list),
    path('students/<int:pk>', api.student_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
