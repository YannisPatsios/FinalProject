from .models import Property
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import *

#########################################################################
## Cart
def cart(request):
    cart = request.session.get('cart', {})
    properties = Property.objects.filter(id__in=cart.keys())
    cart_items = [{'property': property, 'quantity': cart[str(property.id)]} for property in properties]
    return render(request, 'home/cart.html', {'cart_items': cart_items})

def add_to_cart(request, item_id):
    cart = request.session.get('cart', {})
    if item_id in cart:
        cart[item_id] += 1
    else:
        cart[item_id] = 1
    request.session['cart'] = cart
    messages.success(request, "Item added to cart!")
    return redirect('home:home')

def remove_from_cart(request, item_id):
    cart = request.session.get('cart', {})
    if str(item_id) in cart:  # Ensure item_id is treated as a string for comparison
        del cart[str(item_id)]  # Remove the item from the cart
        request.session['cart'] = cart
        messages.success(request, "Item removed from cart!")
    else:
        messages.error(request, "Item not found in cart.")
    return redirect('home:cart')

def main_view(request):
    cart_item_count = 0
    if request.user.is_authenticated:
        # Assuming you have a Cart model and a related name or similar logic
        cart = Cart.objects.filter(user=request.user).first()
        if cart:
            cart_item_count = cart.items.count()  # Adjust based on your actual model
    context = {
        'cart_item_count': cart_item_count,
        # Add other context variables if needed
    }
    return render(request, 'main.html', context)
#########################################################################
## User Authentication
def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful. You are now logged in.")
            return redirect('home:home')
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = SignUpForm()

    return render(request, 'home/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You are now logged in.")
                return redirect('home:home')
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'home/login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home:home')

#########################################################################
## HOME
def home(request):
    query = request.GET.get('q', '')
    properties = Property.objects.all()

    if query:
        properties = properties.filter(name__icontains=query)

    return render(request, 'home/home.html', {'properties': properties, 'query': query})
