from django import forms  
from .models import School, Course



class SchoolForm(forms.Form):
	error_css_class = 'error'
	CATEGORIES = (  
	('UTD', 'UT Dallas'),
	('TAMU', 'Texas A&M'),
	('UT', 'UT Austin'),
	('RICE', 'Rice'),
	)
	category = forms.ChoiceField(choices=CATEGORIES, required=True )
	school = forms.ChoiceField(choices = CATEGORIES)