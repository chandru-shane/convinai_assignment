from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.SalesForceUser)
admin.site.register(models.SalesForceAccount)
admin.site.register(models.SalesForceContact)
