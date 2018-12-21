from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        "author": 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'Blog Content 1',
        'date_posted': 'August 27, 2018'
    },
    {
        "author": 'Jhon Doe',
        'title': 'Blog Post 2',
        'content': 'Blog Content 2',
        'date_posted': 'August 27, 2018'
    },
    {
        "author": 'James King',
        'title': 'Blog Post 3',
        'content': 'Blog Content 3',
        'date_posted': 'August 27, 2018'
    },
    {
        "author": 'CoreyMS',
        'title': 'Blog Post 4',
        'content': 'Blog Content 4',
        'date_posted': 'August 27, 2018'
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})