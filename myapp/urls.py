from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('remind', remind_me, name='remind_me')
]

