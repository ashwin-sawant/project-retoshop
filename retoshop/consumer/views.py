# from django.shortcuts import render

# def userdashboard(request):
#     return render(request, "userdashboard.html")


# def userorder(request):
#     return render(request, "userorder.html")

from django.shortcuts import render, redirect

# Static user data (mocking a database)
USER = {
    'username': 'johndoe',
    'email': 'johndoe@example.com',
    'first_name': 'John',
    'last_name': 'Doe',
}

def user_dashboard(request):
    return render(request, 'userdashboard.html', {'user': USER})

def edit_profile(request):
    if request.method == 'POST':
        # In a real application, here you'd update the user's profile in the database
        USER['first_name'] = request.POST.get('first_name')
        USER['last_name'] = request.POST.get('last_name')
        USER['email'] = request.POST.get('email')
        return redirect('user_dashboard')

    return render(request, 'edit_profile.html', {'user': USER})


# Static user order data for now
ORDERS = [
    {'order_id': 1, 'date': '2024-09-01', 'total': 299.99, 'status': 'Shipped'},
    {'order_id': 2, 'date': '2024-09-10', 'total': 49.99, 'status': 'Pending'},
    # Add more orders here...
]

def userorder(request):
    # Static user data or you can use session data if available
    user_order = ORDERS  # This should be fetched based on user in a real application
    return render(request, 'userorder.html', {'orders': user_order})
