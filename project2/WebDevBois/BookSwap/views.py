from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre, User
from django.views import generic


def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available=BookInstance.objects.all().count()
    num_authors=Author.objects.count()  # The 'all()' is implied by default.
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
    )

def browse(request):
	return render(
		request,
		'browse.html',
		context={},
		)

def profileSelf(request):
	return render(
		request,
		'profileSelf.html',
		context={},
		)

def addBook(request):
    return render(
        request,
        'addBook.html',
        context={},
        )