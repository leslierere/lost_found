from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
def index(request):
    return render(request, './info/site_list.html') #diff


# def register(request):
#     form = UserCreationForm
#     context = {'form': form}
#     return render(request, 'registration/register.html', context)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})