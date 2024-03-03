from django.db import models

# Create your models here.

class Contact(models.Model):
      name=models.CharField(max_length=50)
      email=models.EmailField()
      phone=models.CharField(max_length=10)
      subject=models.CharField(max_length=50)
      message=models.TextField()



class Appointment(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    message=models.TextField()
    age=models.CharField(max_length=10)
    gender=models.CharField(max_length=10)
    address=models.TextField()
    date=models.DateField(null=True)
    time=models.TimeField()

class Gallery(models.Model):
    image=models.ImageField(upload_to='img')

class Packages(models.Model):
    image=models.ImageField(upload_to='img')
    description=models.CharField(max_length=255)
    def __str__(self):
        return self.description

class Subpackage(models.Model):
      name=models.CharField(max_length=50)
      t1=models.CharField(max_length=50)
      t2=models.CharField(max_length=50)
      t3=models.CharField(max_length=50)
      t4=models.CharField(max_length=50)
      t5=models.CharField(max_length=50)
      cost=models.CharField(max_length=50)

      image=models.ImageField(upload_to='img')
      package=models.ForeignKey(Packages,on_delete=models.CASCADE)
      image=models.ImageField(upload_to='img')
      description=models.CharField(max_length=255)

      def ___str__(self):
            return self.description
      

class Blog(models.Model):
    image=models.ImageField(upload_to='img')
    description=models.CharField(max_length=255)
    def __str__(self):
        return self.description
    


class Sub_blog(models.Model):
    image=models.ImageField(upload_to='img')
    name=models.CharField(max_length=50)
    heading1=models.CharField(max_length=500)
    description1=models.CharField(max_length=500)
    heading2=models.CharField(max_length=500)
    description2=models.CharField(max_length=500)
    heading3=models.CharField(max_length=500)
    description3=models.CharField(max_length=500)
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)

class Branch(models.Model):
    image=models.ImageField(upload_to='img')
    description=models.CharField(max_length=255)




class  Enquiry(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    message=models.TextField()