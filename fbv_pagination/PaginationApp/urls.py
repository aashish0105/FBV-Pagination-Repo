from django.urls import path
from .views import *
urlpatterns=[
    path('display/',posts_display_view,name='display'),
]