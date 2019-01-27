from django.db import models

CATEGORIES = (  
('UTD', 'UT Dallas'),
('TAMU', 'Texas A&M'),
('UT', 'UT Austin'),
('RICE', 'Rice'),
)

# Create your models here.
class Course(models.Model):
	subject_name = models.CharField(max_length=200)
	course_number = models.CharField(max_length=200)
	
	def __str__(self):
		return self.course_name
		
class School(models.Model):
	school_name = models.CharField(max_length=200)
	
	def __str__(self):
		return self.course_name
		