from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    products = Product.objects.filter(user=request.user)
    productCounts = products.count()
    context = {
        'name': request.user.username,
        'class': 'PBP KI',
        'app_name' : 'InventLaris',
        'products' : products,
        'last_login': request.COOKIES['last_login'],
        'product_count': productCounts,
        
    }

    return render(request, 'main.html', context)

@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

@login_required(login_url='/login')
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/login')
def get_product_json(request):
    product_item = Product.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))

@login_required(login_url='/login')
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

@login_required(login_url='/login')
def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def register(request):
    form = UserCreationForm()  
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
        
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

@login_required(login_url='/login')
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/login')
def edit_product(request, id):
    # Get product by ID
    product = Product.objects.get(pk = id)

    # Set product as instance of form
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Save the form and return to home page
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form, 'ids': id}
    return render(request, "edit_product.html", context)

@login_required(login_url='/login')
def delete_product(request, id):
    # Get data by ID
    product = Product.objects.get(pk=id)
    # Delete data
    product.delete()
    # Return to the main page
    return HttpResponseRedirect(reverse('main:show_main'))


@login_required(login_url='/login')
def increment_product(request, id):
    product = Product.objects.get(pk=id)
    product.amount += 1
    product.save()

    return HttpResponseRedirect(reverse('main:show_main'))

@login_required(login_url='/login')
def decrement_product(request, id):
    product = Product.objects.get(pk=id)
    product.amount -= 1
    
    if product.amount == 0:
        product.delete()
        return HttpResponseRedirect(reverse('main:show_main'))
    
    else: 
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))




@login_required(login_url='/login')
def get_product_json(request):
    product_item = Product.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))

@login_required(login_url='/login')
@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        amount = request.POST.get("amount")
        user = request.user

        new_product = Product(name=name, price=price, description=description, user=user, amount=amount)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()