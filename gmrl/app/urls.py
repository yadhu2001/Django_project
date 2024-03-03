from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('test',views.test,name='test'),
   path('package',views.package,name='package'),
    path('blog',views.blog,name='blog'),
    path('gallery',views.gallery,name='gallery'),
     path('branches',views.branches,name='branches'),
       path('contactus',views.contactus,name='contactus'),
        path('appointment',views.appointment,name='appointment'),
           path('department',views.department,name='department'),
             path('testimoinal',views.testimoinal,name='testimoinal'),
              path('privacy',views.privacy,name='privacy'),
                   path('terms',views.terms,name='terms'),
                      path('subpackage/<int:id>/',views.subpackage,name='subpackage'),
                              path('subblog/<int:id>/',views.subblog,name='subblog'),
]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
