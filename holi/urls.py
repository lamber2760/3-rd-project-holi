from holi import views  
from django.urls import path

urlpatterns = [
    path("",views.homepage),
    path("aboutus",views.aboutus, name="aboutus"),
    path("contactus",views.contactusx, name="contactusx"),
    path("check_form",views.check_form, name="check_form")
]    
