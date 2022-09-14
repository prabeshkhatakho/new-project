from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.



def home(request):
   
    return render (request, "home.html")

def registration(request):
   
    return render (request, "registration.html")


def login_view(request):

    return render (request, "login.html")

def student_detail(request):
    stu = Student.objects.get(id=1)
    serializer = StudentSerializer(stu)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')








