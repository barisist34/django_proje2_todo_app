from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required

# My models
from todo_app.models import Todo,Category,Tag

@login_required(login_url="/admin/login/")
def home_view(request):
    user=request.user
    # todos=Todo.objects.all()
    todos=Todo.objects.filter(user=request.user)
    todos_active=Todo.objects.filter(is_active=True,title__icontains="api")
    count=todos.count()
    context=dict(
        todos=todos,
        todos_active=todos_active,
        count=count,
        user=user,
    )
    return render(request,'todo_app/todo_list.html',context)

@login_required(login_url="/admin/login/")
def category_view(request,slug_category): # home_view ile benzer
    user=request.user
    category=get_object_or_404(Category,slug=slug_category)
    # todos=Todo.objects.filter(category=category,is_active=True)
    #todos=Todo.objects.filter(category=category,is_active=True,user=request.user)
    #todos=category.todo_set.all()
    todos=category.todo_set.filter(user=request.user) 
    context=dict(
        todos=todos,
        category=category,
        user=user,
    )
    #print(f"todos: {todos.first().title}")
    print(f"category : {category}")
    return render(request,'todo_app/todo_list.html',context)


def category_reverse(request,slug_category):
    categories=Category.objects.get(slug=slug_category)
    context=dict(
        categories=categories,
    )
    return render(request,"todo_app/category_reverse.html",context)

@login_required(login_url="/admin/login/")
def todo_detail_view(request,slug_category,id):
    user=request.user
    # todo_detail=Todo.objects.get(id=id)
    todo_first=Todo.objects.first()
    # todo_detail=get_object_or_404(Todo,category__slug=slug_category,id=id)
    todo_detail=get_object_or_404(Todo,category__slug=slug_category,id=id,user=request.user)
    context=dict(
        todo_detail=todo_detail,
        user=user,
    )
    print(f"todo_first.category:  {todo_first.category} ")
    print(f"todo_first.category.slug:  {todo_first.category.slug} ")
    return render(request,"todo_app/todo_detail.html",context)
#şş

@login_required(login_url="/admin/login/")
def tag_view(request,slug_tag):
    tag=get_object_or_404(Tag,slug=slug_tag)
    todos=tag.todo_set.filter(user=request.user)
    context=dict(
        todos=todos,
        tag=tag,
    )
    return render(request,'todo_app/todo_list.html',context)
