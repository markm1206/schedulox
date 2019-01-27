from django.urls import path

from . import views
app_name = 'schedulox'
urlpatterns = [
    path('', views.index, name='index'),
	path('schoolSelect',views.schoolSelect,name='schoolSelect'),
	path('courseSelect',views.courseSelect,name='courseSelect'),
	path('addCourse',views.addCourse,name='addCourse')
	]