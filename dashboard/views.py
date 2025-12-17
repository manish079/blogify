from django.shortcuts import render
from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm, BlogPostForm
from django.shortcuts import get_object_or_404, redirect
from django.utils.text import slugify


@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()

    context = {
        'category_count': category_count,
        'blogs_count': blogs_count,
    }   
    return render(request, 'dashboard/dashboard.html', context)


############### Category ########################

def categories(request):
    # categories = Category.objects.all()  # already into context
    # context = {
    #     'categories': categories,
    # }
    return render(request, 'dashboard/categories.html')


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST) # I can also use request.data.name for getting data
        if form.is_valid():
            form.save()
            return redirect('categories')

    form = CategoryForm()  # <input type="text" name="category_name" maxlength="255" required id="id_category_name">
    
    context = {
        'form': form,
    }
        
    return render(request, 'dashboard/add_category.html', context)

def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=category)
    context = {
        'form': form,
        'category': category,
    }
    return render(request, 'dashboard/edit_category.html', context)

def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')   

############## Post ########################

def posts(request):
    posts = Blog.objects.all().order_by('-updated_at')
    context = {
        'posts': posts,
    }
    return render(request, 'dashboard/posts.html', context)

def add_post(request):
    
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        
        if form.is_valid():
            post = form.save(commit = False) # Temporarily save the form without committing to DB
            post.author = request.user     # Assign the logged-in user as the author
            
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-' + str(post.id)

            post.save()
            return redirect('posts')

        else:
            print('form is invalid')
            print(form.errors)
    
    form = BlogPostForm()
    context = {
        'form': form,
    }
    
    return render(request, 'dashboard/add_post.html', context)

def edit_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-'+str(post.id)
            post.save()
            return redirect('posts')
    form = BlogPostForm(instance=post)
    context = {
        'form': form,
        'post': post
    }
    return render(request, 'dashboard/edit_post.html', context)


def delete_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.delete()
    return redirect('posts')

    