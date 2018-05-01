from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances
from django.contrib.auth.models import User

import datetime




# Basic Model layout:

# class MyModelName(models.Model):
#     """
#     A typical class defining a model, derived from the Model class.
#     """

#     # Fields
#     my_field_name = models.CharField(max_length=20, help_text="Enter field documentation")
#     ...

#     # Metadata
#     class Meta: 
#         ordering = ["-my_field_name"]

#     # Methods
#     def get_absolute_url(self):
#          """
#          Returns the url to access a particular instance of MyModelName.
#          """
#          return reverse('model-detail-view', args=[str(self.id)])
    
#     def __str__(self):
#         """
#         String for representing the MyModelName object (in Admin site etc.)
#         """
#         return self.field_name

class Genre(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    BOOK_GENRES = (
        ('Fiction','Fiction'),
        ('Non-Fiction','Non-Fiction'),
        ('Textbook','Textbook'),
        ('History','History'),
        ('Mystery','Mystery'),
        ('Sci-Fi','Sci-Fi'),
    )

    name = models.CharField(max_length=200, choices=BOOK_GENRES, blank=True, default='Fiction', help_text="Select a book genre (e.g. Science Fiction, French Poetry etc.)")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Book(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this book")

    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    for_class = models.CharField('Class', max_length=200, help_text='Enter which class this textbook is for.', default='Not for a class.')

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title
    
    
    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this book.
        """
        return reverse('book-detail', args=[str(self.id)])

    class Meta:
        unique_together = (('title', 'author'),)

class BookInstance(models.Model):
    """
    Model representing a specific copy of a book (i.e. that can be borrowed from the library).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True) 
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    instance_pic = models.TextField(default='https://i.imgur.com/0l2uZR9.jpg')


    CONDITION = (
        ('5','Like-New'), ('4','Good'), ('3','Average'), ('2','Bad'), ('1','Barely Readable'),
    )

    book_condition = models.CharField(max_length=1, choices=CONDITION, blank=True, default='5', help_text='Book condition')
    comment = models.CharField(max_length=500, default='', help_text='Additional comments about your book (e.g. pricing, books you want to swap it for, etc).')

    class Meta:
        ordering = ["book_condition"]
        

    def __str__(self):
        """
        String for representing the Model object
        """
        return '{0} ({1})'.format(self.id,self.book.title)

class Author(models.Model):
    """
    Model representing an author.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ["last_name","first_name"]
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('author-detail', args=[str(self.id)])
    

    def __str__(self):
        """
        String for representing the Model object.
        """
        return str(self.first_name + " " + self.last_name)

    class Meta:
        unique_together = (('first_name', 'last_name'),)

class Profile(models.Model):
	"""
	Model representing each user in the system.
	"""
	user = models.OneToOneField(User, on_delete=models.CASCADE, default='None')
	SCHOOLS = (
		('University of Massachusetts Amherst','University of Massachusetts Amherst'),
		('Hampshire College', 'Hampshire College'),
		('Smith College', 'Smith College'),
		('Mount Holyoke College', 'Mount Holyoke College'),
		('Amherst College', 'Amherst College'),
		('Other','Other'),
		('None', 'None'),
	)
	university = models.CharField(max_length=200, choices=SCHOOLS, blank=True, default='None', help_text='School or University')
	bio = models.CharField(max_length=200, help_text="Enter a short bio.")

    
	# books_offered = models.ForeignKey('BookInstance', on_delete=models.CASCADE, null=True)
	books_wanted = models.ManyToManyField(Book) 

	# class Meta:
	# 	ordering = ["last_name","first_name"]

	def get_absolute_url(self):
		return reverse('user-detail', args=[str(self.user.username)])
    
	def __str__(self):
		return '{0}, {1}'.format(self.user.first_name,self.user.last_name)

class Message(models.Model):
    """
    Model representing each user in the system.
    """
    text = models.CharField(max_length=1000, blank=True, default='None', help_text='Message')

    message_from = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='msg_from')
    message_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='msg_to')

    date_sent = models.DateTimeField(help_text="Date of Message Sent")
    
    def __str__(self):
        return '{0}'.format(self.text)

