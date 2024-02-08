from django.contrib import admin
from .models import *
# Register your models here.

class Enquiry(admin.ModelAdmin):
    list_display=['name','email','phone','message']

class Pack(admin.ModelAdmin):
    list_display=['name','image']

class Event_details(admin.ModelAdmin):
    list_display=['image','description']

class Gal_display(admin.ModelAdmin):
    list_display=['image']

class Contactus_display(admin.ModelAdmin):
    list_display=['name','phone','email','subject','message']

class Sub(admin.ModelAdmin):
    list_display=['image','price','day','night','pack']

class Event1(admin.ModelAdmin):
    list_display=['image','event']

class Sup(admin.ModelAdmin):
    list_display=['destination','day','night','price','description','destination1','destination2','destination3','desc1','desc2','desc3','image1','image2','image3','pack']

admin.site.register(Contact,Enquiry)
admin.site.register(Package,Pack)
admin.site.register(Event,Event_details)
admin.site.register(Gal,Gal_display)
admin.site.register(Contactus,Contactus_display)
admin.site.register(Subpackage,Sub)
admin.site.register(Event_news,Event1)
admin.site.register(Subpack,Sup)
