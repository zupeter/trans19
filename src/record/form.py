from django.forms import ModelForm
from .models import *

class CaseForm(ModelForm):
	class Meta:
		model = CaseRecord
		fields = ['name','id_number','date_of_birth','date_of_comfirmed','case_number']


class LocationForm(ModelForm):
	class Meta:
		model = LocationRecord
		fields = ['location','address','district','x_coord','y_coord','detail','category']
		#idk how to make this form, this class looks very different from the tutorial you sent us#


class VisitForm(ModelForm):
	class Meta:
		model = VisitRecord
		fields = ['location','date_from','date_to','case']
