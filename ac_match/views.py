from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'smth',
        'title': 'blog post 1',
        'content': 'first post content',
        'date_posted': 'smth'
    },
    {
        'author': 'jane',
        'title': 'blog post 2',
        'content': 'second post content',
        'date_posted': 'smth2'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'ac_match/home.html', context)



def about(request):
    return render(request, 'ac_match/about.html', {'title': 'About'})