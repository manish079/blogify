from django.shortcuts import render
from django.http import JsonResponse



# def home(request):
#     return JsonResponse({'message': 'Welcome to Blogify!'})

def home(request):
    return render(request, 'home.html')