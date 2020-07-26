from django.shortcuts import render
from .models import Post

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
        'posts': Post.objects.all(),
        'show_sidebar': True
    }
    return render(request, 'ac_match/home.html', context)



def about(request):
    return render(request, 'ac_match/about.html', {'title': 'About', 'show_sidebar': False})