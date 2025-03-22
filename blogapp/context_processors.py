from .models import Category

def category_menu(request):
    """
    Returns category list for global template context
    """
    return {
        #Return a dictionary containing the category list.
        'cat_menu': Category.objects.all().order_by('name')
    }