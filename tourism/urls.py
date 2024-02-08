from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('packages/',views.packages,name='packages'),
    path('news/',views.news,name='news'),
    path('gallery/',views.gallery,name='gallery'),
    path('contact/',views.contact,name='contact'),
    path('subpack/<int:id>/',views.Subpackages,name='subpack'),
    path('testimonials',views.test,name='testimonials'),
    path('event/<int:id>/',views.event,name='event'),
    path('subpack1/<int:id>/',views.subpack,name='subpack1'),
   
]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)