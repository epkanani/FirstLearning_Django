from django.shortcuts import render
from django.http import HttpResponse # type: ignore

# Create your views here.
# my first basic view object

# basic test to make sure our request function works
# def index(request):
#     return HttpResponse('Hello Elvis you have successfuly run your first view ')

# Now am going insert the dynamic value required to be rendered in index.html file using the key value pair
def index(request):
    my_dictionary = {"insert_val":"hello you inserted me from view.py! and in a new first_app/index.html"}
    return render(request,"first_app/index.html",context=my_dictionary)