from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog, Category

def posts_by_category(request, category_id):
    posts = Blog.objects.filter(status='Published', category=category_id)
   
    # Use get_object_or_404 when you want to show 404 error page if the category does not exist
    category = get_object_or_404(Category, pk=category_id)
    
    context = {
        'posts': posts,
        'category': category,
    }
    
    return render(request, 'posts_by_category.html', context)