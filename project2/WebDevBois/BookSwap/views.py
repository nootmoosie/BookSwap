from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre, User
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
    Jack = User.objects.get(first_name="Jack")
    queryset = BookInstance.objects.filter(owner = Jack.id)
    
    return render(request,'browse.html', context={'queryset':queryset},)

def profileSelf(request):
	user = User.objects.get(first_name="Nate")
	otherUser = User.objects.get(first_name="Jack")
	booksOffer = BookInstance.objects.filter(owner = user.id)
	booksWant = user.books_wanted.all()
	recommended = BookInstance.objects.filter(owner = otherUser.id) #This needs fixing
	
	paginator = Paginator(booksOffer, 3)
	page = request.GET.get('page', 1)
	books = paginator.get_page(page)
	
	

	return render(
		request,
		'profileSelf.html',
		context={'user': user, 'booksWant': booksWant, 'books': books,
		 'recommended':recommended[0],},
		)

def addBook(request):
	return render(
		request,
		'addBook.html',
		context={},
		)

def profileOther(request):
	user = User.objects.get(first_name="Jack")
	booksOffer = BookInstance.objects.filter(owner = user.id)
	wishlist = user.books_wanted.all()


	paginator = Paginator(booksOffer, 3)
	page = request.GET.get('page', 1)
	books = paginator.get_page(page)

	return render(
		request,
		'profileOther.html',
		context={'user':user, 'books':books, 'wishlist':wishlist},
		)

def contact(request):
	return render(
		request,
		'contact.html',
		context={},
		)