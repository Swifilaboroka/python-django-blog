from django.shortcuts import render
from django.http import HttpResponse
from .models import Post   
# Create your views here.
posts = [
    {
        'author' : 'Mark',
        'title'  : 'Django Web Development',
        'content': 'with Django so you can develop things rapidly, without having to deal with configuring a production server',
        'date_posted' : 'Auguest 27, 2018'
    },
    {
        'author' : 'Wembo Mulumba Otepa',
        'title'  : 'Artificial Intelligence',
        'content': 'with Django so you can develop things rapidly, without having to deal with configuring a production server',
        'date_posted' : 'December 21, 2018'
    },

    {
        'author' : 'Wembo Mulumba Otepa',
        'title'  : 'C++ Programming',
        'content': 'with Django so you can develop things rapidly, without having to deal with configuring a production server',
        'date_posted' : 'December 28, 2018'
    }
]

def home(request):
    #return HttpResponse('<h1>Blog Home</h1>')
    context = {
        #'posts' : posts
        'posts' : posts.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})

def contact(request):
    return HttpResponse('<h1>Contact Blog Author</h1>')    

#blog -> templates -> blog -> template.html 

#blog -> templates -> blog -> template.html
