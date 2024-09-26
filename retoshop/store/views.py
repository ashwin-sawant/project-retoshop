from django.shortcuts import render, get_object_or_404, redirect
from .models import Category

# def store(request):
#     categories = Category.objects.all()
#     return render(request, "store.html",{'categories':categories})

def products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.all()  # Get all products related to this category
    return render(request, 'category_products.html', {'category': category, 'products': products})

def product(request):
    return render(request, "particular_product.html")

# # from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

# # Product List View (Store/Home Page)
# def store(request):
#     products = Product.objects.all()  # Get all products
#     return render(request, 'store.html', {'products': products})

# # Add to Cart View
# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     cart = request.session.get('cart', {})
#     cart[product_id] = cart.get(product_id, 0) + 1  # Increment quantity
#     request.session['cart'] = cart
#     return redirect('view_cart')

# # View Cart
# def view_cart(request):
#     cart = request.session.get('cart', {})
#     products = Product.objects.filter(id__in=cart.keys())
#     cart_items = [(product, cart[str(product.id)]) for product in products]
    
#     total_price = sum(product.price * quantity for product, quantity in cart_items)
    
#     return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

# # Remove from Cart View
# def remove_from_cart(request, product_id):
#     cart = request.session.get('cart', {})
#     if str(product_id) in cart:
#         del cart[str(product_id)]
#     request.session['cart'] = cart
#     return redirect('view_cart')



# Static category data (mocking a database)
CATEGORIES = [
    {'id': 1, 'name': 'Electronics', 'description': 'Gadgets, devices, and more'},
    {'id': 2, 'name': 'Clothing', 'description': 'Men\'s and women\'s fashion'},
    {'id': 3, 'name': 'Home Appliances', 'description': 'Appliances for your home'},
]

# Static products data (mocking a database)
PRODUCTS = [
    {'id': 1, 'category_id': 1, 'name': 'Laptop', 'description': 'High-performance laptop', 'price': 999.99, 'image': 'laptop.jpg'},
    {'id': 2, 'category_id': 1, 'name': 'Smartphone', 'description': 'Latest smartphone', 'price': 799.99, 'image': 'smartphone.jpg'},
    {'id': 3, 'category_id': 2, 'name': 'T-shirt', 'description': 'Cotton t-shirt', 'price': 19.99, 'image': 'tshirt.jpg'},
    {'id': 4, 'category_id': 3, 'name': 'Washing Machine', 'description': 'Efficient washing machine', 'price': 399.99, 'image': 'washing_machine.jpg'},
]

# Store view - Display categories
def store(request):
    return render(request, 'store.html', {'categories': CATEGORIES})

# Products view - Display products of a selected category
def products_view(request, category_id):
    category_products = [product for product in PRODUCTS if product['category_id'] == category_id]
    category_name = next((cat['name'] for cat in CATEGORIES if cat['id'] == category_id), "Category")
    return render(request, 'products.html', {'products': category_products, 'category_name': category_name})


# # Product List View (Store/Home Page)
# def store(request):
#     return render(request, 'store.html', {'products': PRODUCTS})

# Add to Cart View
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1  # Increment quantity
    request.session['cart'] = cart

    # Store the last category visited in the session
    category_id = request.GET.get('category_id')
    if category_id:
        request.session['category_id'] = category_id
    
    return redirect('view_cart')

# View Cart
def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0
    category_id = request.session.get('category_id', None)  # Retrieve the last category from the session
    
    for product in PRODUCTS:
        product_id = str(product['id'])
        if product_id in cart:
            quantity = cart[product_id]
            product_total = product['price'] * quantity
            cart_items.append({'product': product, 'quantity': quantity, 'total': product_total})
            total_price += product_total

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price, 'category_id': category_id})

# Remove from Cart View
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
    request.session['cart'] = cart
    return redirect('view_cart')
