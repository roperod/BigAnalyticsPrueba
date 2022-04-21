from django.shortcuts import redirect, render

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

# AUTHENTICATION
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            print("User Authenticated")
            login(request, form.get_user())
            return redirect('/../show/')
        else:
            return redirect('/login')
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {'form': form})

def user_logout(request):
    logout(request)
    return redirect('/login')
