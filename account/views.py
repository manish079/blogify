from django.shortcuts import render
from django.http import JsonResponse
from blogs.models import Category, Blog
from account.models import About, SocialLink


def home(request):
    # categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True, status="Published").order_by('updated_at')
    posts = Blog.objects.filter(status="Published", is_featured=False).order_by('-updated_at')
    
    try:
      about = About.objects.get()
    except:
      about = None
    context = {
        # 'categories': categories, # No need we are using this using context processor(shared across all templates)
        'featured_posts': featured_posts,
        'posts': posts,
        'about': about,
    }
    return render(request, 'home.html', context)