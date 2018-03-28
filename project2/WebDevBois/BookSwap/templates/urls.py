from django.urls import path
from . import views


urlpatterns = [
    path('', views.addBook, name='addBook'),
    path('', views.browse, name='browse'),
    path('', views.home, name='home'),
    path('', views.profileOther, name='profileOther'),
    path('', views.profileSelf, name='profileSelf'),
]