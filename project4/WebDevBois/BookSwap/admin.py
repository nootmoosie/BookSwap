from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Profile, Message

# Register your models here.

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)
admin.site.register(Profile)
admin.site.register(Message)