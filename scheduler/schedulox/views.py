from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from .models import School,Course
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
	
def addCourse(request):
	"""html = "<button><a class='button2'>test</a></button>"
	return HttpResponse(html)
	now = datetime.datetime.now()
	t = Template("<html><body>It is now {{ current_date }}.</body></html>")
	html = t.render(Context({'current_date': now}))
	return HttpResponse(html)"""
	return render_to_response(template='example.html')
