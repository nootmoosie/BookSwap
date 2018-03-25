from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances



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
        ('f','Fiction'),
        ('n','Non-Fiction'),
        ('t','Textbook'),
        ('h','History'),
        ('m','Mystery'),
        ('h','History'),
        ('s','Sci-Fi'),
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
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN',max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
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

class BookInstance(models.Model):
    """
    Model representing a specific copy of a book (i.e. that can be borrowed from the library).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True) 

    CONDITION = (
        ('5','Like-New'), ('4','Good'), ('3','Average'), ('2','Bad'), ('1','Barely Readable'),
    )

    book_condition = models.CharField(max_length=1, choices=CONDITION, blank=True, default='5', help_text='Book condition')
    owner = models.OneToOneField('User', on_delete=models.SET_NULL, null=True)
    comments = models.CharField(max_length=500, help_text='Any additional comments about your book (e.g. pricing, reason for getting rid of it, etc).')

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
        return '{0}, {1}'.format(self.last_name,self.first_name)

class User(models.Model):
	"""
	Model representing each user in the system.
	"""
	#id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular user")
	first_name = models.CharField(max_length=200, help_text="Enter your first name.")
	last_name = models.CharField(max_length=200, help_text="Enter your last name.")
	university = models.CharField(max_length=200, help_text="Enter your school or university.")
	bio = models.CharField(max_length=200, help_text="Enter a short bio.")

	books_offered = models.ManyToManyField(Book, help_text="THIS IS INCORRECT") #fix this later.
	books_wanted = models.ManyToManyField(Book, help_text="THIS IS INCORRECT") #fix this later.

	class Meta:
		ordering = ["last_name","first_name"]

	def get_absolute_url(self):
		return reverse('user-detail', args=[str(self.id)])
    
	def __str__(self):
		return '{0}, {1}'.format(self.first_name,self.last_name)
