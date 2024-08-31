from django.shortcuts import render
from .forms import AddUserForm
from account.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.set_password(request.POST.get('password'))
            user.save()

            if user.role == User.USER: 
                group = Group.objects.get(name='User')
                group.user_set.add(user)
            
            messages.success(request, 'Registration successful. Please log in to proceed.')

            return redirect('account:login')
    else:
        form = AddUserForm()

    return render(request, 'chat/add_user.html', {
        'form': form
    })