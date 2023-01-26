

from django.contrib import admin

from .models import Custumer, Malaria, Message, GetMalaria, Palu,Avc,Prediction

# Register your models here.
admin.site.register([Custumer,Message,Malaria,GetMalaria,Palu,Avc,Prediction])

