from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
    path('', views.addBook, name='addBook'),
    path('', views.browse, name='browse'),
    path('', views.profileOther, name='profileOther'),
    path('', views.profileSelf, name='profileSelf'),
]