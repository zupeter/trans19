from django.db import models

# Create your models here.
class CaseRecord(models.Model):
	name				= models.CharField(max_length=255)
	id_number 			= models.CharField(max_length=30,unique=True)
	date_of_birth 		= models.DateField()
	date_of_comfirmed	= models.DateField()
	case_number			= models.PositiveIntegerField(unique=True)


class LocationRecord(models.Model):
	location		= models.CharField(max_length=127)
	address			= models.CharField(max_length=255, null=True, blank=True)
	district		= models.CharField(max_length=20, default='Hong Kong')
	x_coord			= models.DecimalField(max_digits=22, decimal_places=16, null=True)
	y_coord			= models.DecimalField(max_digits=22, decimal_places=16, null=True)
	category		= models.CharField(max_length=30)


class VisitRecord(models.Model):
	location		= models.ForeignKey(CaseRecord, on_delete=models.PROTECT)
	date_from		= models.DateField()
	date_to			= models.DateField()
	detail			= models.CharField(max_length=127, null=True, blank=True)
	
