from .models import NavItem

def navbar_data(request):
    navitem = NavItem.objects.all()  # Fetch all NavItem objects
    return {'navitem': navitem} 