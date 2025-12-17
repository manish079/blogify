from .models import Category
from account.models import SocialLink

# used across the apps 
def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)

def get_social_links(request):
    social_links = SocialLink.objects.all()
    return dict(social_links=social_links)

def user_name_initials(request):
    user = request.user
    if user.is_authenticated:
        full_name = user.get_full_name().strip()
        username = user.username

        if full_name:
            parts = full_name.split()
            # if more than one name, show first & last
            if len(parts) >= 2:
                display_name = f"{parts[0]} {parts[-1]}"
            else:
                display_name = parts[0]
        else:
            # if no full name set, use username
            display_name = username

        # compute initials
        names = display_name.split()
        if len(names) == 1:
            initials = (names[0][0] + (names[0][1] if len(names[0])>1 else "")).upper()
        else:
            initials = (names[0][0] + names[1][0]).upper()

        return {
            'display_name': display_name,
            'initials': initials,
        }

    return {}


