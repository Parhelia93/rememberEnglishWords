from django import forms
from .models import *


class AddWordCategory(forms.Form):
    title = forms.CharField(max_length=255, label='Category Name',
                            widget=forms.TextInput(attrs={'class': 'form-input'}))
    slug = forms.SlugField(max_length=255, label='Slag Name')
    description = forms.CharField(max_length=255, label='Some Description')
    is_published = forms.BooleanField(label='Published', initial=True)
    progress_cat = forms.ModelChoiceField(queryset=ProgressCat.objects.all(),
                                          label='Categoty',
                                          empty_label='Not chose')


class AddWord(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['word_cat'].empty_label = 'Not chose'

    class Meta:
        model = Word
        #fields = '__all__'
        fields = {'word', 'translation', 'slug', 'example', 'word_cat'}
        widgets = {
            'word':forms.TextInput(attrs={'class':'form-input'}),
            'description':forms.Textarea(attrs={'cols':60, 'rows':10})
        }

