from django.http import  HttpResponse
from django.shortcuts import render

from .forms import ContactForm


def home_page(request):
	context={
	 	"title":"from views.py home_page",
	 	"content":"Welcome to the homepage"
	}
	return render(request, "home_page.html", context)

def about_page(request):
	context={
	 	"title":"from views.py about_page",
	 	"content":"Welcome to the aboutpage"
	}
	return render(request, "about_page.html", context)


def contact_page(request):
	contact_form = ContactForm(request.POST or None)
	context={
	 	"title":"from views.py contact_page",
	 	"content":"Welcome to the contactpage",
	 	"form":contact_form
	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)
	# Test on fields form_contact
	#if request.method == "POST":
		#print(request.POST)
		#print(request.POST.get('fullname'))
		#print(request.POST.get('email'))
		#print(request.POST.get('content'))
	#...........................................
	return render(request, "contact/view.html", context)


