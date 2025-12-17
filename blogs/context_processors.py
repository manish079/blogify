from .models import Category
from account.models import SocialLink

# used across the apps 
def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)

def get_social_links(request):
    social_links = SocialLink.objects.all()
    return dict(social_links=social_links)

