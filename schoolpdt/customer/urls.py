from django.urls import path
from .  import views
urlpatterns=[
    path('',views.HoMe,name='home')
]