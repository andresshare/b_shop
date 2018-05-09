from django.http import  HttpResponse
from django.shortcuts import render


def home_page(request):
	context={
	 	"title":"message: from views.py home_page",
	 	"content":"Welcome to the homepage"
	}
	return render(request, "home_page.html", context)

def about_page(request):
	context={
	 	"title":"message: from views.py about_page",
	 	"content":"Welcome to the aboutpage"
	}
	return render(request, "about_page.html", context)


def contact_page(request):
	context={
	 	"title":"message: from views.py contact_page",
	 	"content":"Welcome to the contactpage"
	}
	return render(request, "contact_page.html", context)


