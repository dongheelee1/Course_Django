from django.shortcuts import render, HttpResponse, redirect
from .models import Course

# Create your views here.
def index(request):
	courses = Course.objects.all()
	print courses
	context = {
		'courses': courses
	}
	return render(request, 'courses/index.html', context)
def process_course(request):
	print request.POST
	Course.objects.create(name=request.POST['name'],description=request.POST['description'])
	return redirect('/')
def remove_course(request, course):
	print course
	Course.objects.filter(id=course).delete()
	return redirect('/')