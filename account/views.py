from django.shortcuts import render, redirect
from django.http import JsonResponse
from blogs.models import Category, Blog
from account.models import About, SocialLink
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


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


def signup(request):
    if request.method == 'POST':
      
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        
        if not username or not password or not email:
            messages.error(request, "All fields are required")
            return redirect('register')
        
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Enter a valid email address")
            return render(request, 'register.html')
                
        if User.objects.filter(email=email).exists():
            messages.error(request, "User with this email already exists")
            return redirect('register')
    
        user = User.objects.create_user(username=username, password=password, email=email)
        messages.success(request, "User registered successfully")

        return redirect('login')
          
    return render(request, 'register.html')   


def login(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username')
        password = request.POST.get('password')

        if not username_or_email or not password:
            messages.error(request, "All fields are required")
            return render(request, 'login.html')

        if "@" in username_or_email:
            try:
                validate_email(username_or_email)
            except ValidationError:
                # Stop here with email message
                messages.error(request, "Enter a valid email address")
                return render(request, 'login.html')

        # Try authenticate with username first
        user = authenticate(request, username=username_or_email, password=password)

        # If not authenticated & input looks like email, try email login
        if user is None and "@" in username_or_email:
            try:
                user_obj = User.objects.get(email=username_or_email)
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                user = None

        if user:
            auth.login(request, user)
            messages.success(request, "Login successful")
            return redirect('dashboard') 

        messages.error(request, "Invalid credentials")
        return render(request, 'login.html')

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('home')