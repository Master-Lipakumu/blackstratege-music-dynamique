
from django.urls import path, include

from .views import index, contacte


urlpatterns = [
    
    path('', index, name="index"),
    path('contacte/', contacte, name="contacte"),
    

]
