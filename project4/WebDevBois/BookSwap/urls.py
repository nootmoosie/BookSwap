from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
    path('browse', views.browse, name='browse'),
    path('addBook', views.add_book, name='addBook'),
    path('addWishlist', views.add_Wishlist, name='addWishlist'),
    path('profiles/<int:pk>', views.profileOther, name='profileOther'), 
    path('profile', views.profileSelf, name='profileSelf'),
    path('contact', views.contact, name='contact'),
	path('profile/editBio', views.edit_bio, name='editBio'),
<<<<<<< HEAD
	path('profile/messages', views.messages, name='messages')
=======
	path('profile/messages', views.messages, name='messages'),
	path('profiles/<int:pk>/sendMessage', views.sendMessage, name='sendMessage'), #does this even work....??
>>>>>>> 864d800bde3ad8a06d193fe88a7e8bf9180c7a44
]