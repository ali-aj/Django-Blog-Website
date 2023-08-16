from django.shortcuts import render, redirect
from .models import blogData, contactUs
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    blog_data = blogData.objects.all().values()
    user = request.user.username
    return render(request, 'home.html', {'blog_data': blog_data, 'active': 'home', 'user': user}) 

@login_required
def contact_us(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        ins = contactUs(name=name, email=email, message=message)
        ins.save()
    return render(request, 'contact.html', {'active': 'contact_us'})
    
@login_required    
def about(request):
    return render(request, 'about.html', {'active': 'about'})

@login_required    
def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        image1 = request.FILES['image1'] 
        image2 = '' 
        image3 = '' 
        username = request.user.username
        if 'image2' in request.FILES:
            image2 = request.FILES['image2'] 
        if 'image3' in request.FILES:
            image3 = request.FILES['image3']
        ins = blogData(title=title, desc=description, image1=image1, image2=image2, image3=image3, owner_username=username)
        ins.save()
    return render(request, 'create.html', {'active': 'create'})

@login_required    
def display_blog(request, blog_id):
    blog_data = blogData.objects.filter(id=blog_id).values()[0]
    return render(request, 'display_blog.html', {'blog_data': blog_data})

@login_required    
def my_blogs(request):
    username = request.user.username
    blog_data = blogData.objects.filter(owner_username=username).values()
    return render(request, 'my_blogs.html', {'blog_data': blog_data, 'active': 'my_blogs'})

@login_required
def delete_blog(request, blog_id):
    blog = blogData.objects.get(id=blog_id)
    blog.delete()
    return redirect('/my_blogs')