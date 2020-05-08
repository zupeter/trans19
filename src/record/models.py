from django.db import models

# Create your models here.
class CaseRecord(models.Model):
	name				= models.CharField(max_length=255)
	id_number 			= models.CharField(max_length=30,unique=True)
	date_of_birth 		= models.DateField()
	date_of_comfirmed	= models.DateField()
	case_number			= models.PositiveIntegerField(unique=True)

	def __str__(self):
		return f"Case {self.pk}"

	def get_absolute_url(self):
		# print(f"/case/{self.case_number}")
		return f"/case/{self.pk}"	

	def get_edit_url(self):
		return f"{self.get_absolute_url()}/modify"

	def get_delete_url(self):
		return f"{self.get_absolute_url()}/delete"



class LocationRecord(models.Model):
	location		= models.CharField(max_length=127)
	address			= models.CharField(max_length=255, null=True, blank=True)
	district		= models.CharField(max_length=20, default='Hong Kong')
	x_coord			= models.DecimalField(max_digits=22, decimal_places=4, null=True)
	y_coord			= models.DecimalField(max_digits=22, decimal_places=4, null=True)
	detail			= models.CharField(max_length=127, null=True, blank=True)
	category		= models.CharField(max_length=30)

	def __str__(self):
		return f"{self.location} in {self.district}"

	def get_location_absolute_url(self):
		return f"/location/{self.pk}"

	def get_location_modify_url(self):
		return f"/location/{self.pk}/modify"

	def get_location_delete_url(self):
		return f"/location/{self.pk}/delete"


class VisitRecord(models.Model):
	location		= models.ForeignKey(LocationRecord, on_delete=models.PROTECT)
	date_from		= models.DateField()
	date_to			= models.DateField()
	case 			= models.ForeignKey(CaseRecord, on_delete=models.CASCADE)
