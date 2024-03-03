from django.contrib import admin
from . models import *
# Register your models here.



class Enquiry_display(admin.ModelAdmin):
    list_display=['name','email','phone','message']


class Contact_display(admin.ModelAdmin):
    list_display=['name','email','phone','message','subject']


class Gallery_display(admin.ModelAdmin):
    list_display=['image']


class Packages_display(admin.ModelAdmin):
    list_display=['image','description']


class Appointment_display(admin.ModelAdmin):
    list_display=['name','email','phone','message','date','time','address','gender','age']

class Subpackage_display(admin.ModelAdmin):
    list_display=['image','t1','t2','t3','t4','t5','name','cost']   


class Blog_display(admin.ModelAdmin):
    list_display=['image','description'] 

class Sub_blog_display(admin.ModelAdmin):
    list_display=['name','image','heading1','description1','heading2','description2','heading3','description3','blog']

class Branch_display(admin.ModelAdmin):
    list_display=['image','description']

admin.site.register(Contact,Contact_display)
admin.site.register(Appointment,Appointment_display)
admin.site.register(Gallery,Gallery_display)
admin.site.register(Packages,Packages_display)
admin.site.register(Subpackage,Subpackage_display)
admin.site.register(Blog,Blog_display)
admin.site.register(Sub_blog,Sub_blog_display)
admin.site.register(Branch,Branch_display)
admin.site.register(Enquiry,Enquiry_display)
