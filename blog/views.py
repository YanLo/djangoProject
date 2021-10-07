from django.shortcuts import render
# Create your views here.

posts = [
    {
        'author': 'Yan',
        'title': 'post1',
        'content': 'dummy data',
        'date_posted': '7 Oct 2021'
    },
    {
        'author': 'YanLo',
        'title': 'post2',
        'content': 'dummy data 2',
        'date_posted': '9 Oct 2021'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
