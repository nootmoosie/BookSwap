from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
    path('browse', views.browse, name='browse'),
    # path('', views.addBook, name='addBook'),
    # path('', views.profileOther, name='profileOther'),
    path('profile', views.profileSelf, name='profileSelf'),
]