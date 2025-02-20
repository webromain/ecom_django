from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import User, UserForm

from django.contrib import messages

def home(request):
    featured_product = Product.objects.filter(name__icontains='Cambridge').first()
    latest_products = Product.objects.filter(available=True)
    if featured_product:
        latest_products = latest_products.exclude(id=featured_product.id)
    latest_products = latest_products.order_by('-created')[:7]
    
    return render(request, 'home.html', {
        'featured_product': featured_product,
        'latest_products': latest_products
    })

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    if request.method == "GET":
        research = request.GET.get('research')
        if research is not None:
            products = products.filter(name__icontains=research)
    
    return render(request, 'products/product_list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    
    return render(request, 'products/product_detail.html', {
        'product': product,
        'related_products': related_products
    })

def register_(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account is created !")
            return redirect('login')
    return render(request, 'logreg/register.html', {'form':form})

def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, "You are connected !")
            return redirect('product_list')
        else:
            messages.error(request, "Your email or your password are incorrect")
    return render(request, 'logreg/login.html')

@login_required(login_url='/login/')
def log_out(request):
    logout(request)
    return redirect('login')

def profil(request):
    return render(request, 'profil/profil.html')
