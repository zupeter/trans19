from django.contrib import admin

# Register your models here.


from .models import *


admin.site.register(CaseRecord)
admin.site.register(LocationRecord)
admin.site.register(VisitRecord)