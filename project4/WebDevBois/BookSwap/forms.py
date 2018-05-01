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
    for_class = forms.CharField(label = "College Class? (If no leave blank)", required = False)
    url = forms.CharField(label = "Image URL", required = False)

    def clean_title(self):
        data = self.cleaned_data['title']
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

    def clean_for_class(self):
        data = self.cleaned_data['for_class']
        return data

    def clean_url(self):
        data = self.cleaned_data['url']
        return data


class AddWishlistForm(forms.Form):


    title = forms.CharField(label = "Title", min_length = 1, required = True)
    author_first = forms.CharField(label = "Author's First Name", min_length = 1, required = True)
    author_last = forms.CharField(label = "Author's Last Name", min_length = 1, required = True)
    genre = forms.ModelChoiceField(queryset = Genre.objects.all())
    for_class = forms.CharField(label = "College Class? (If no leave blank)", required = False)


    def clean_title(self):
        data = self.cleaned_data['title']

        return data

    def clean_author_first(self):
        data = self.cleaned_data['author_first']
        return data

    def clean_author_last(self):
        data = self.cleaned_data['author_last']
        return data

    def clean_genre(self):
        data = self.cleaned_data['genre']
        return data

class EditBioForm(forms.Form):

    COLLEGE_CHOICES = Profile.SCHOOLS

    college = forms.ChoiceField(choices = COLLEGE_CHOICES, label="College/University", widget=forms.Select(), required=True)
    bio = forms.CharField(label = "Bio", min_length = 1, widget=forms.Textarea, required = True)


    def clean_college(self):
        data = self.cleaned_data['college']
        return data

    def clean_bio(self):
        data = self.cleaned_data['bio']
        return data

class MessageForm(forms.Form):

    msg = forms.CharField(label = "Message", min_length = 1, widget=forms.Textarea, required = True)

    def clean_msg(self):
        data = self.cleaned_data['msg']
        return data