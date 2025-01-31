from django.shortcuts import render, get_object_or_404
from .models import Category, Product

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
