from django.contrib.auth import authenticate, login

from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm, Login_Form


def home_page(request):
    context = {'title': 'from views.py home_page',
               'content': 'Welcome to the homepage'}
    return render(request, 'home_page.html', context)


def about_page(request):
    context = {'title': 'from views.py about_page',
               'content': 'Welcome to the aboutpage'}
    return render(request, 'about_page.html', context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {'title': 'from views.py contact_page',
               'content': 'Welcome to the contactpage',
               'form': contact_form}
    if contact_form.is_valid():
        print (contact_form.cleaned_data)

    # Test on fields form_contact
    # if request.method == "POST":
        # print(request.POST)
        # print(request.POST.get('fullname'))
        # print(request.POST.get('email'))
        # print(request.POST.get('content'))
    # ...........................................

    return render(request, 'contact/view.html', context)


def login_page(request):
    form = Login_Form(request.POST or None)
    context = {
    'form': form
    }
    print('User logged in')
    #print (request.user.is_authenticated())
    if form.is_valid():
        print (form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username,
                            password=password)
        print(user)
        #print (request.user.is_authenticated())
        if user is not None:
        #print (request.user.is_authenticated())
            login(request, user)

        # Redirect to a success page.

        #context['form'] = Login_Form()
            return redirect('/login')
        else:

        # Return an 'invalid login' error message.

            print ('error')
    return render(request, 'auth/login.html', context)


def register_page(request):
    form = Login_Form(request.POST or None)
    if form.is_valid():
        print (form.cleaned_data)
    return render(request, 'auth/register.html', {})
