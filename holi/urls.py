from holi import views  
from django.urls import path

urlpatterns = [
    path("",views.homepage),
    path("aboutus",views.aboutus, name="aboutus"),
    path("form",views.formx, name="formx"),
    path("check_form",views.check_form, name="check_form"),

    path("mydata",views.savethis, name="savethis")
    
]    
