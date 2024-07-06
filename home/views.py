from django.shortcuts import render
from .models import Post
# Create your views here.

def home(request):
    context = {
        'objects' : Post.objects.all
    }
    return render(request, 'index.html',context)

