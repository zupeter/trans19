from django import forms
from .models import *

class CaseForm(forms.ModelForm):
	class Meta:
		model = CaseRecord
		fields = ['name','id_number','date_of_birth','date_of_comfirmed','case_number']


class LocationForm(forms.ModelForm):
	class Meta:
		model = LocationRecord
		fields = ['location','address','district','x_coord','y_coord']
		#idk how to make this form, this class looks very different from the tutorial you sent us#


class VisitForm(forms.ModelForm):
	class Meta:
		model = VisitRecord
		fields = ['location','date_from','date_to','case','detail','category']


class SearchForm(forms.Form):
	window = forms.IntegerField(label='Search Window of time (in days)')


