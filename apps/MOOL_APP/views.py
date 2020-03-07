from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Restaurant, Product, Order, Setup
from datetime import date

def login(request):
    if 'admin' in request.session:
        del request.session['admin']
    return render(request, "MOOL_APP/login.html")

def log_in(request):
    if request.method == "POST":
        if request.POST['password'] == 'mool.won':
            request.session['admin'] = True
            return redirect("/main")
        else:
            return redirect('/')

def main(request):
    if 'admin' not in request.session:
        return redirect('/')
    else:
        context = {
            "all_restaurants": Restaurant.objects.all(),
            "all_products": Product.objects.all()
        }
        return render(request, "MOOL_APP/main.html", context)

def new_restaurant(request):
    if 'admin' not in request.session:
        return redirect('/')
    else:
        return render(request, "MOOL_APP/new_restaurant.html")

def create_restaurant(request):
    if 'admin' not in request.session:
        return redirect('/')
    else:
        if request.method == "POST":
            errors = Restaurant.objects.basic_validator(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value)
                return redirect('/new_restaurant')
            else:
                new_rest = Restaurant.objects.create(name = request.POST['name'], number = request.POST['yourphone'], date = request.POST['date'], code = request.POST['code'])
                new_rest.save()
                return redirect('/main')
        else:
            return redirect('/new_restaurant')

def update_restaurant(request, id):
    if 'admin' not in request.session:
        return redirect('/')
    else:
        restaurant = Restaurant.objects.get(id = id)
        context = {
            "restaurant": restaurant,
            "date": restaurant.date.strftime("%Y-%m-%d")
        }
        return render(request, "MOOL_APP/update_restaurant.html", context)

def edit_restaurant(request, id):
    if 'admin' not in request.session:
        return redirect('/')
    else:
        if request.method == "POST":
            errors = Restaurant.objects.basic_validator(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value)
                return redirect('/update_restaurant/'+id)
            else:
                edit_rest = Restaurant.objects.get(id = id)
                edit_rest.name = request.POST['name']
                edit_rest.number = request.POST['yourphone']
                edit_rest.date = request.POST['date']
                edit_rest.code = request.POST['code']
                edit_rest.save()
                return redirect('/main')
        else:
            return redirect('/update_restaurant/'+id)

def delete_restaurant(request, id):
    if 'admin' not in request.session:
        return redirect('/')
    else:
        this_restaurant = Restaurant.objects.get(id = id)
        this_restaurant.delete()
        return redirect('/main')

def new_product(request):
    if 'admin' not in request.session:
        return redirect('/')
    else:
        restaurants = Restaurant.objects.all()
        context = {
            "restaurants": restaurants
        }
        return render(request, "MOOL_APP/new_product.html", context)

def create_product(request):
    if 'admin' not in request.session:
        return redirect('/')
    else:
        if request.method == "POST":
            errors = Product.objects.basic_validator(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value)
                return redirect('/new_product')
            else:
                new_product = Product.objects.create(name = request.POST['name'], quantity = request.POST['quantity'])
                new_product.save()
                for id in range(0,len(request.POST.getlist('checks[]'))):
                    print(new_product.setup)
                    restaurant = Restaurant.objects.get(id = request.POST.getlist('checks[]')[id])
                    new_setup = Setup.objects.create(restaurant = restaurant, product = new_product, price = request.POST.getlist('price[]')[id])
                    new_setup.save()
                return redirect('/main')

def update_product(request, id):
    if 'admin' not in request.session:
        return redirect('/')
    else:
        product = Product.objects.get(id = id)
        context = {
            "product": product,
            "restaurants": Restaurant.objects.all(),
            "setups": Setup.objects.filter(product = product),
        }
        return render(request, "MOOL_APP/update_product.html", context)

def edit_product(request, id):
    if 'admin' not in request.session:
        return redirect('/')
    else:
        if request.method == "POST":
            errors = Product.objects.basic_validator(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value)
                return redirect('/update_product/'+id)
            else:
                edit_prod = Product.objects.get(id = id)
                edit_prod.name = request.POST['name']
                edit_prod.quantity = request.POST['quantity']
                all_restaurants = Restaurant.objects.all()
                for restaurant in all_restaurants:
                    edit_prod.restaurants.remove(restaurant)                    
                for id in request.POST.getlist('checks[]'):
                    restaurant = Restaurant.objects.get(id = id)
                    edit_prod.restaurants.add(restaurant)
                edit_prod.save()
                return redirect('/main')
        else:
            return redirect('/update_product/'+id)

def delete_product(request, id):
    if 'admin' not in request.session:
        return redirect('/')
    else:
        this_product = Product.objects.get(id = id)
        this_product.delete()
        return redirect('/main')

def today_order(request):
    if 'admin' not in request.session:
        return redirect('/')
    else:
        context = {
            "products": Product.objects.all(),
            "restaurants": Restaurant.objects.all(),
        }
        return render(request, 'MOOL_APP/today_order.html', context)