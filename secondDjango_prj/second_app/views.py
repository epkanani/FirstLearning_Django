from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore

# Create your views here.
# basic test just to make sure the code is running successful
def index(request):
    return HttpResponse('Hello Elvis you have successfuly run your first view ')

# Now will use the templates here to render our html and the template tags to include dynamic content
def help(request):
    my_dictionary = {"insert_val":"hello you inserted me from view.py! and in a new second_app/help.html"}
    return render(request,"help.html",context=my_dictionary)