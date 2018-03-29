from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre, User
from django.views import generic


def index(request):
    """
    View function for home page of site.
    """
    queryset = BookInstance.objects.all()[:3]
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'queryset':queryset},
    )

def browse(request):
    queryset = BookInstance.objects.all()[:]
    
    return render(request,'browse.html', context={'queryset':queryset},)

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
def profileOther(request):
	user = User.objects.get(first_name="Nate")
	books = BookInstance.objects.filter(owner = user.id)
	return render(
		request,
		'profileOther.html',
		context={'user':user, 'books':books},
		)