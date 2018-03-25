from django.db import models

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
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name