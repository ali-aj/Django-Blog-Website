from django import forms

class loginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'username', 'placeholder': 'Enter your username', 'name': 'username'}))
    password = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password', 'placeholder': 'Enter your Password', 'name': 'password'}))
    
    
class signUpForm(forms.Form):
    username = forms.CharField(label='Your username', max_length=100)
    password = forms.CharField(label='Your Password', min_length=8)
    email = forms.EmailField()