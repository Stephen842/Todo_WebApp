from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ['title', 'details', 'date'] 
        widget = {
                'title': forms.TextInput(attrs = {'class': 'title2', 'placeholder': 'Enter Title'}),
                'details': forms.Textarea(attrs = {'class': 'details', 'placeholder': 'Enter Description'}),
                'completed': forms.CheckboxInput(attrs = {'class': 'checkbox'}),
                'date': forms.DateInput(attrs = {'class': 'date'})
                }

class SearchForm(forms.Form):
    search_query = forms.CharField(max_length = 250)

