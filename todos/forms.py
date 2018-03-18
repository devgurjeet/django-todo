from django import forms


class TodoForm(forms.Form):
    text = forms.CharField(max_length=100,
                           label='',
                           widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Enter todo here.'}),)


