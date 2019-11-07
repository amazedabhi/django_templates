from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    developed_by = "Arpit Pandey"
    friends= [
        "Abhinav",
        "Arpit",
        "Brajesh",
        "Pulkit",
        "Shubham"
    ]
    show_friends = True

    context = {
        "developer": developed_by,
        "friends": friends,
        "show_friends": show_friends
    }
    response = render(request,'HelloWorld/index.html',context)
    return response

def hello(request):
    return render(request, 'HelloWorld/hello.html')
