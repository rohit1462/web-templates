from django.shortcuts import render
from registration.forms import signup_form
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.forms import ValidationError


# Create your views here.

def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            # fm = signup_form(request.POST)
            fm = signup_form(request.POST)
        
            if fm.is_valid():
                fm.save()
                messages.success(request,'Hi {} Account Created Successfully !!'.format(fm.cleaned_data.get('username')))
                return HttpResponseRedirect('/login/')
        else:
            fm = signup_form()
        
        fm.label_suffix = ''
        fm.fields['username'].widget.attrs['placeholder'] = 'enter username'
        fm.fields['password1'].widget.attrs['placeholder'] = 'enter password'
        fm.fields['password2'].widget.attrs['placeholder'] = 'confirm password'

        return render(request,'signup.html',context={'form':fm})
    else:
        return HttpResponseRedirect('/profile/')

def check_login(request):
    if request.user.is_authenticated:
        print("already login")
        return HttpResponseRedirect('/profile/')
    else:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            try:
                if fm.is_valid():
                    uname = fm.cleaned_data.get('username')
                    upass = fm.cleaned_data.get('password')
                    user = authenticate(username=uname, password=upass)
                    if user is not None:
                        login(request, user)
                        return HttpResponseRedirect('/profile/')
                else:
                    raise fm.get_invalid_login_error()
            except ValidationError:
                messages.error(request,'Invalid Credentials')
                fm = AuthenticationForm()
                
        else:
            fm = AuthenticationForm()
            
        fm.label_suffix=''
        fm.fields['username'].widget.attrs['placeholder'] = 'enter username'
        fm.fields['password'].widget.attrs['placeholder'] = 'enter password'
        return render(request,'login.html',context={'form':fm})

def show_profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html',context={'name':request.user.username})
    else:
        return HttpResponseRedirect('/login/')

def show_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect('/login/')

def show_change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'{} your password has changed successfully !!'.format(request.user.username))
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user=request.user)
        fm.label_suffix = ''
        fm.fields['old_password'].widget.attrs['placeholder'] = 'enter old password'
        fm.fields['new_password1'].widget.attrs['placeholder'] = 'enter new password'
        fm.fields['new_password2'].widget.attrs['placeholder'] = 'confirm new password'

        return render(request,'changepassword.html',context={'form':fm})
    else:
        return HttpResponseRedirect('/login/')

def show_reset_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'{} your password has reseted successfully !!'.format(request.user.username))
                return HttpResponseRedirect('/profile/')
        else:
            fm = SetPasswordForm(user=request.user)
        fm.label_suffix = ''
        # fm.fields['old_password'].widget.attrs['placeholder'] = 'enter old password'
        fm.fields['new_password1'].widget.attrs['placeholder'] = 'enter new password'
        fm.fields['new_password2'].widget.attrs['placeholder'] = 'confirm new password'

        return render(request,'passwordreset.html',context={'form':fm})
    else:
        return HttpResponseRedirect('/login/')

def show_home(request):
    return render(request,'home.html')

