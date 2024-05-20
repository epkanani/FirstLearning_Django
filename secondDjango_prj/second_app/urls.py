# included libraries
from django.urls import path # type: ignore
from . import views

# our url patterns function
urlpatterns = [
    path("",views.help, name="help"),  
]