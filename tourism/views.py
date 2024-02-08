from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
# Create your views here.

def index(request):
    
    context={}
    con=Package.objects.all()
    context["con"]=con
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')

        if request.POST:
            details=Contact.objects.create(name=name,email=email,phone=phone,message=message)
            details.save()
            return redirect('index')
        
    

    

    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')


def packages(request):

    context={}
    obj=Package.objects.all()
    context['obj']=obj
    return render(request,'packages.html',context)

    


def news(request):
    context={}
    eve=Event.objects.all()
    context['eve']=eve
    return render(request,'news.html',context)

def gallery(request):
    context={}
    gal=Gal.objects.all()
    context['gal']=gal
    return render(request,'gallery.html',context)


def contact(request):
    context={}
    con=Contactus.objects.all()
    context["con"]=con
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        subject=request.POST.get('subject')

        if request.POST:
            details=Contactus.objects.create(name=name,email=email,phone=phone,message=message,subject=subject)
            details.save()
            return redirect('index')
        
    return render(request,'contact.html',context)

def Subpackages(request,id):
    
    context={}
    sp=Package.objects.all()
    sub=Subpackage.objects.all().filter(id=id)
    context['sub']=sub
    context['sp']=sp
    return render(request,'subpack.html',context)


def test(request):
    return render(request,'testimonials.html')

def event(request,id):
    context={}
    eve=Event.objects.all()
    sp=Event_news.objects.all().filter(id=id)
    context['eve']=eve
    context['sp']=sp
    return render(request,'event.html',context)

def subpack(request,id):
    context={}
    sup=Subpack.objects.all().filter(pack=id)
    
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        requirement=request.POST.get('requirement')
        

        if request.POST:
            details=Contactus.objects.create(name=name,email=email,phone=phone,message=requirement)
            details.save()
            return redirect('packages')
    context["sup"]=sup

    return render(request,'subpack1.html',context)
