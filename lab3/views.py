from django.shortcuts import render,redirect,resolve_url
from django.urls import path
import random
from django.http import HttpRequest,HttpResponse
from .models import books
from .forms import booksForm


def home_pa(requst):
    home_pa: str="Welcom to my webside"
    return render(requst,"lab3/enter.html",{"welcome":home_pa} )
def about_us(requst):
    about_us: str=" senior student at AOU Major CS \n in Dean's list for academic perfomance twice "
    return render(requst,"lab3/about.html",{"info":about_us} )

# Create your views here.
def add_book(request : HttpRequest):# same function but add if contion
    if request.method == "POST":
        new_book = booksForm(request.POST , request.FILES)

        if new_book.is_valid():
            new_book.save()
            return redirect(resolve_url("lab3:added"))


    form = booksForm()

    return render(request, 'lab3/add_book.html', {"form" : form})

def home(request : HttpRequest):

    bo = books.objects.all()

    return render(request, 'lab3/index.html', {"books" : bo})

def book_added(request : HttpRequest):
        return render(request, 'lab3/thanks.html')
def Games(request : HttpRequest):
        return render(request, 'lab3/Games.html')

def AI(request : HttpRequest):
        return render(request, 'lab3/Minesweeper.html')

def academic_marks(request : HttpRequest):
        return render(request ,'lab3/academic_marks.html')

def search(request : HttpRequest):
        return render( request, 'lab3/search.html')

def Django(request : HttpRequest):
        return render( request, 'lab3/Django.html')