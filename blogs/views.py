from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog, Category, Comment
from django.db.models import Q

def posts_by_category(request, category_id):
    posts = Blog.objects.filter(status='Published', category=category_id)
   
    # Use get_object_or_404 when you want to show 404 error page if the category does not exist
    category = get_object_or_404(Category, pk=category_id)
    
    context = {
        'posts': posts,
        'category': category,
    }
    
    return render(request, 'posts_by_category.html', context)


def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')
    
    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        if comment_text:
            comment = Comment()
            comment.user = request.user
            comment.blog = single_blog
            comment.comment = comment_text
            comment.save()
            
            return HttpResponseRedirect(request.path_info)
    
    comments = Comment.objects.filter(blog=single_blog).order_by('-updated_at')
    comment_count = comments.count()      
            
    context = {
        'single_blog' : single_blog,
        'comments' : comments,
        'comment_count' : comment_count,
    }
    
    return render(request, 'blogs.html', context)


def search_blogs(request):
    
    keyword = request.GET.get('keyword')
    
    # blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(description__icontains=keyword), status='Published'
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status = "Published")
    
    
    context = {
        'blogs' : blogs,
        'keyword' : keyword,
    }
    
    return render(request, 'search_blogs.html', context)