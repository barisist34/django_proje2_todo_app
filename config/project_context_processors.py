from todo_app.models import Category

def global_context(request):

    global_categories=Category.objects.all().filter(is_active=True)
    
    return dict(
        global_categories=global_categories,
        user=request.user,
    )