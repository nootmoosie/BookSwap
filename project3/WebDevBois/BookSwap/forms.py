from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime #for checking renewal date range.

from .models import Book, Author, BookInstance, Genre, Profile
    
class AddBookForm(forms.Form):
    # renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    CONDITION_CHOICES = BookInstance.CONDITION

    # GENRE_CHOICES = (
    #     (1, _("")),
    #     (2, _("Bad")),
    #     (3, _("Fair")),
    #     (4, _("Good")),
    #     (5, _("Great"))
    #     )

    #Author
    #Book - Genre, ForClass
    #BookInst - Picture

    title = forms.CharField(label = "Title", min_length = 1, required = True)
    author_first = forms.CharField(label = "Author's First Name", min_length = 1, required = True)
    author_last = forms.CharField(label = "Author's Last Name", min_length = 1, required = True)
    condition = forms.ChoiceField(choices = CONDITION_CHOICES, label="Conditon", initial='', widget=forms.Select(), required=True)
    genre = forms.ModelChoiceField(queryset = Genre.objects.all())
    comments = forms.CharField(label = "Comments (Optional)", required = False)


    def clean_title(self):
        data = self.cleaned_data['title']
        #Check date is not in past. 
        # if data < datetime.date.today():
        #     raise ValidationError(_('Invalid date - renewal in past'))

        # #Check date is in range librarian allowed to change (+4 weeks).
        # if data > datetime.date.today() + datetime.timedelta(weeks=4):
        #     raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data

    def clean_author_first(self):
        data = self.cleaned_data['author_first']
        return data

    def clean_author_last(self):
        data = self.cleaned_data['author_last']
        return data

    def clean_condition(self):
        data = self.cleaned_data['condition']
        return data

    def clean_genre(self):
        data = self.cleaned_data['genre']
        return data

    def clean_comments(self):
        data = self.cleaned_data['comments']
        return data