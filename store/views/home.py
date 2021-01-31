#module for page render and redirect
from django.shortcuts import render, redirect
#module for Http responce genaration
from django.http import HttpResponse
#module for password hashing so that admin can't see the user password
from django.contrib.auth.hashers import make_password, check_password

#import the model class which is used here
from store.models.product import Product
from store.models.category import Category
# from .models.customer import Customer





######################################### Create your views here ############################################################




#index method when base or home urls hit the this method will runing and serve the adjacent html page

def index(request):
    # return HttpResponse('<h1>Index Page</h1>')
    products=None
    categories = Category.get_all_categories()
    categoryId = request.GET.get('category')
    if categoryId:
        products=Product.get_all_product_by_id(categoryId)
    else:
        products=Product.get_all_products()
    data={}
    data['products'] = products
    data['categories']=categories
    return render(request,'index.html',data)
    # return render(request,'orders/order.html')
