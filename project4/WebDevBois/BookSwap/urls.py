from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', views.index, name='index'),
    path('browse', views.browse, name='browse'),
    path('addBook', views.add_book, name='addBook'),
    path('addWishlist', views.add_Wishlist, name='addWishlist'),
    path('profiles/<int:pk>', views.profileOther, name='profileOther'), 
    path('profile', views.profileSelf, name='profileSelf'),
    path('contact', views.contact, name='contact'),
	path('profile/editBio', views.edit_bio, name='editBio'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)