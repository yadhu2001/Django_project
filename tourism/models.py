from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    message=models.TextField()


class Package(models.Model):
    name=models.CharField(max_length=255)
    image = models.ImageField(upload_to='img')
    
    def __str__(self):
        return self.name

class Event(models.Model):
    image=models.ImageField(upload_to='img')
    description=models.CharField(max_length=255)

    def __str__(self):
        return self.description

class Gal(models.Model):
    image=models.CharField(max_length=3000)

class Contactus(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    message=models.TextField()
    subject=models.CharField(max_length=255)

class Subpackage(models.Model):
    image = models.ImageField(upload_to='img')
    price=models.CharField(max_length=50)
    day=models.CharField(max_length=10)
    night=models.CharField(max_length=10)
    pack=models.ForeignKey(Package,on_delete=models.CASCADE)
    def __str__(self):
        return self.price
class Event_news(models.Model):
    image=models.ImageField(upload_to='img')
    event=models.ForeignKey(Event,on_delete=models.CASCADE)

class Subpack(models.Model):
     destination=models.CharField(max_length=50)
     day=models.CharField(max_length=20)
     night=models.CharField(max_length=20)
     price=models.CharField(max_length=20)
     description=models.CharField(max_length=255)
     destination1=models.CharField(max_length=20)
     destination2=models.CharField(max_length=20)
     destination3=models.CharField(max_length=20)
     desc1=models.CharField(max_length=255)
     desc2=models.CharField(max_length=255)
     desc3=models.CharField(max_length=255)
     image1=models.ImageField(upload_to='uploads/')
     image2=models.ImageField(upload_to='uploads/')
     image3=models.ImageField(upload_to='uploads/')
     pack=models.ForeignKey(Subpackage, on_delete=models.CASCADE)
     
    