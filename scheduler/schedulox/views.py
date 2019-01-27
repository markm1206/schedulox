from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from .models import School
from .forms import SchoolForm
from django.shortcuts import render

def index(request):
	return render(request, 'schedulox/index.html')

def schoolSelect(request):
	#school  = get_object_or_404(School, pk=school_name)
	#school = request.GET['schoolSelector'] 
	#print(school)
	form = SchoolForm(request.POST or None)
	answer = ''
	if form.is_valid():
		answer = form.cleaned_data.get('school')
	print(answer)
	return render(request, 'schedulox/schoolSelect.html')
	
def courseSelect(request):
	return render(request, 'schedulox/courseSelect.html')