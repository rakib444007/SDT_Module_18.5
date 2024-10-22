from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistrationForm,ChangeUserForm
# Create your views here.



def signup(request):
    if request.method == 'POST':
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,'Account Created successfully')
            return redirect('signup')
    else:
        register_form = RegistrationForm()
    return render(request,'signup.html',{'form' : register_form ,'type' : 'SignUp'})

        

def user_login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request,request.POST)
        if login_form.is_valid():
            user_name=login_form.cleaned_data['username']
            user_pass = login_form.cleaned_data['password']
            user = authenticate(username=user_name,password = user_pass)
            if user is not None:
                messages.success(request,'Logged In Successfully')
                login(request,user)
                return redirect('profile')
            else:
                
                return redirect('singup')
    else:
        
        login_form = AuthenticationForm()
    return render(request,'user_login.html',{'form' : login_form ,'type' : 'Login'})


@login_required
def user_logout(request):
    messages.success(request,'Logged Out Successfully')
    logout(request)
    return redirect('user_login')

@login_required
def profile(request):
    return render(request,'profile.html')

@login_required
def pass_change1(request):

    if request.method == 'POST':
        change_pass = PasswordChangeForm(user=request.user,data = request.POST)
        if change_pass.is_valid():
            change_pass.save()
            messages.success(request,'Password Updated successfully')
            update_session_auth_hash(request,change_pass.user)
            return redirect('profile')
    else:
        change_pass = PasswordChangeForm(user=request.user)
    return render(request,'passchange1.html',{'form' : change_pass})
@login_required
def pass_change2(request):

    if request.method == 'POST':
        change_pass = SetPasswordForm(user=request.user,data = request.POST)
        if change_pass.is_valid():
            change_pass.save()
            messages.success(request,'Password Updated successfully')
            update_session_auth_hash(request,change_pass.user)
            return redirect('profile')
    else:
        change_pass = SetPasswordForm(user=request.user)
    return render(request,'passchange1.html',{'form' : change_pass})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        edit_form = ChangeUserForm(request.POST,instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request,'Profile Updated Successfully')
            return redirect('profile')
    else:
        edit_form=ChangeUserForm(instance = request.user)
    return render(request,'updateProfile.html',{'form': edit_form})
