from django.db import models

# Create your models here.
class CaseRecord(models.Model):
	name				= models.CharField(max_length=255)
	id_number 			= models.CharField(max_length=20,unique=True)
	date_of_birth 		= models.DateField()
	date_of_comfirmed	= models.DateField()
	case_number			= models.PositiveIntegerField(unique=True)

	def __str__(self):
		return f"Case {self.case_number}"

	def get_absolute_url(self):
		# print(f"/case/{self.case_number}")
		return f"/case/{self.pk}"	

	def get_edit_url(self):
		return f"{self.get_absolute_url()}/modify"

	def get_delete_url(self):
		return f"{self.get_absolute_url()}/delete"
	
	def get_trace_url(self):
		return f"{self.get_trace_url()}/trace"



class LocationRecord(models.Model):
	CENTRALANDWESTERN = 'Central and Western'
	EASTERN = 'Eastern'
	SOUTHERN = 'Southern'
	WANCHAI = 'Wan Chai'

	SHAMSHUIPO = 'Sham Shui Po'
	KOWLOONCITY = 'Kowloon City'
	KWUNTONG = 'Kwun Tong'
	WONGTAISIN = 'Wong Tai Sin'
	YAUTSIMMONG = 'Yau Tsim Mong'

	ISLANDS = 'Islands'
	KWAITSING = 'Kwai Tsing'
	NORTH = 'North'
	SAIKUNG = 'Sai Kung'
	SHATIN = 'Sha Tin'
	TAIPO = 'Tai Po'
	TSUENWAN = 'Tsuen Wan'
	TUENMUN = 'Tuen Mun'
	YUENLONG = 'Yuen Long'

	DISTRICT_CHOICES = [
		(CENTRALANDWESTERN,'Central and Western'),
		(EASTERN,'Eastern'),
		(SOUTHERN,'Southern'),
		(WANCHAI,'Wan Chai'),
		(SHAMSHUIPO,'Sham Shui Po'),
		(KOWLOONCITY,'Kowloon City'),
		(KWUNTONG,'Kwun Tong'),
		(WONGTAISIN,'Wong Tai Sin'),
		(YAUTSIMMONG,'Yau Tsim Mong'),
		(ISLANDS,'Islands'),
		(KWAITSING,'Kwai Tsing'),
		(NORTH,'North'),
		(SAIKUNG,'Sai Kung'),
		(SHATIN,'Sha Tin'),
		(TAIPO,'Tai Po'),
		(TSUENWAN,'Tsuen Wan'),
		(TUENMUN,'Tuen Mun'),
		(YUENLONG,'Yuen Long'),
	]
	location		= models.CharField(max_length=127)
	address			= models.CharField(max_length=255, null=True, blank=True)
	district		= models.CharField(max_length=20, choices=DISTRICT_CHOICES, default=CENTRALANDWESTERN)
	x_coord			= models.DecimalField(max_digits=22, decimal_places=4, null=True)
	y_coord			= models.DecimalField(max_digits=22, decimal_places=4, null=True)
	




	def __str__(self):
		return f"{self.location} in {self.district}"

	def get_location_absolute_url(self):
		return f"/location/{self.pk}"

	def get_location_modify_url(self):
		return f"/location/{self.pk}/modify"

	def get_location_delete_url(self):
		return f"/location/{self.pk}/delete"


class VisitRecord(models.Model):
	case 			= models.ForeignKey(CaseRecord, on_delete=models.CASCADE)
	location		= models.ForeignKey(LocationRecord, on_delete=models.PROTECT)
	date_from		= models.DateField()
	date_to			= models.DateField()
	detail			= models.CharField(max_length=127, null=True, blank=True)
	category		= models.CharField(max_length=30)

