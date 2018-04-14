from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre, Profile
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def index(request):
    """
    View function for home page of site.
    """
    user = User.objects.get(first_name="Jack")
    queryset = BookInstance.objects.filter(owner = user.id)[1:4]
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'queryset':queryset},
    )

@login_required
def browse(request):
	user = request.user
	admin = User.objects.get(username = "compsci326")
	queryset = BookInstance.objects.exclude(owner = user.id).exclude(owner = admin.id)
	otherUser = User.objects.exclude(id = user.id).exclude(username="compsci326")[0]
	

	return render(
		request,
		'browse.html',
		context={'queryset' : queryset, 'user' : user, 'otherUser' : otherUser,},
		)

@login_required
def profileSelf(request):
	use = request.user
	profile = Profile.objects.get(user = use.id)
	otherUser = User.objects.exclude(id = use.id).exclude(username="compsci326")[0]
	booksOffer = BookInstance.objects.filter(owner = use.id)
	booksWant = profile.books_wanted.all()
	recommended = BookInstance.objects.filter(owner = otherUser.id) #This needs fixing
	
	paginator = Paginator(booksOffer, 5)
	page = request.GET.get('page', 1)
	books = paginator.get_page(page)
	
	

	return render(
		request,
		'profileSelf.html',
		context={'user': use, 'profile': profile, 'booksWant': booksWant, 'books': books,
		'recommended':recommended[0], 'otherUser': otherUser,},
		
		)

def profileOther(request, pk):
	user = User.objects.get(id = pk)
	#user = request.user
	profile = Profile.objects.get(user = user.id)
	booksOffer = BookInstance.objects.filter(owner = user.id)
	wishlist = profile.books_wanted.all()


	paginator = Paginator(booksOffer, 5)
	page = request.GET.get('page', 1)
	books = paginator.get_page(page)

	return render(
		request,
		'profileOther.html',
		context={'user':user, 'profile': profile, 'books':books, 'wishlist':wishlist},
		)

def addBook(request):
	return render(
		request,
		'addBook.html',
		context={},
		)



def contact(request):
	return render(
		request,
		'contact.html',
		context={},
		)