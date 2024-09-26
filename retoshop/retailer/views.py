from django.shortcuts import render, redirect


# Static data for demonstration purposes
SHOP = {
    'name': 'Retail Shop',
    'logo': 'shop_logo.jpg',
}

PRODUCTS = [
    {'id': 1, 'name': 'Product 1', 'price': 19.99},
    {'id': 2, 'name': 'Product 2', 'price': 29.99},
    # Add more products here...
]

ORDERS = [
    {'order_id': 1, 'date': '2024-09-01', 'total': 59.99, 'status': 'Shipped'},
    {'order_id': 2, 'date': '2024-09-10', 'total': 29.99, 'status': 'Pending'},
    # Add more orders here...
]

def retailer_dashboard(request):
    if request.method == 'POST':
        # Update shop details based on form data
        SHOP['name'] = request.POST.get('shop_name', SHOP['name'])
        SHOP['logo'] = request.FILES.get('shop_logo', SHOP['logo'])
        # Handle file saving (not implemented here, for simplicity)
    
    return render(request, 'retailer_dashboard.html', {'shop': SHOP})

def add_products(request):
    if request.method == 'POST':
        # Simulate adding a new product
        product_name = request.POST.get('product_name')
        product_price = float(request.POST.get('product_price', 0))
        new_product_id = len(PRODUCTS) + 1
        PRODUCTS.append({'id': new_product_id, 'name': product_name, 'price': product_price})
        return redirect('add_products')

    return render(request, 'add_products.html', {'products': PRODUCTS})

def retailer_orders(request):
    return render(request, 'retailer_orders.html', {'orders': ORDERS})
