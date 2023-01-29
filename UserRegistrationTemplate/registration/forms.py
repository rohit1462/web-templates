from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class signup_form(UserCreationForm):
    # username = forms.CharField(
    #     label='User Name',
    #     label_suffix="",
    #     widget=forms.TextInput(attrs={'placeholder':'enter username'}),
    #     error_messages={'required':'Please enter your username'}
    #     )
    
    first_name = forms.CharField(
        label='First Name',
        # label_suffix="",
        widget=forms.TextInput(attrs={'placeholder':'first name'}),
        error_messages={'required':'this field is required'}
        )
    last_name = forms.CharField(
        label='Last Name',
        # label_suffix="",
        widget=forms.TextInput(attrs={'placeholder':'last name'}),
        error_messages={'required':'this field is required'}
        )
    
    email = forms.EmailField(
        label="Email Address",
        # label_suffix="",
        widget=forms.TextInput(attrs={'placeholder':'enter email'}),
        error_messages={'required':'Please enter your email id'}
        )
    class Meta:
        model = User
        fields =['username','first_name','last_name','email','password1','password2']

    
    # password1 = forms.CharField(
    #     label="Password",
    #     label_suffix="",
    #     widget=forms.PasswordInput(attrs={'placeholder':'enter password'}),
    #     error_messages={'required':'This field is required'}
    #     )
    # password2 = forms.CharField(
    #     label="Confirm Password",
    #     label_suffix="",
    #     widget=forms.PasswordInput(attrs={'placeholder':'enter password'}),
    #     error_messages={'required':'This field is required'}
    #     )
