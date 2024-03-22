from holi import views  
from django.urls import path

urlpatterns = [


    path("",views.homepage),
    path("aboutus",views.aboutus, name="aboutus"),
    path("aboutus",views.aboutus, name="aboutus"),
     

    
]    
