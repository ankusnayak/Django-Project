#module for page render and redirect
from django.shortcuts import render, redirect
#module for Http responce genaration
from django.http import HttpResponse
#module for password hashing so that admin can't see the user password
from django.contrib.auth.hashers import make_password, check_password

#import the model class which is used here
from .models.product import Product
from .models.category import Category
from .models.customer import Customer


from django.views import View


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


def validateCustomer(customer):
    error_message = {}
        
    if (not customer.firstName):
        error_message['firstName'] = "First Name Required!!"
    elif len(customer.firstName) < 4:
            error_message['firstName'] = 'First Name must be 4 char long'
    elif not customer.lastName:
        error_message['lastName'] = "Last Name Required"
    elif len(customer.lastName) < 2:
        error_message['lastName'] = 'Last Name must be 2 char long'
    elif not customer.phone:
        error_message['phone'] = "Phone Number Required"
    elif len(customer.phone) < 10:
        error_message['phone'] = "Phone Number Must be 10 digit long"
    elif not customer.email:
        error_message['email'] = "Email Required" 
    elif customer.isExists():
        error_message['emailvalidation'] = 'Email already exists'

    return error_message    

def registerCustomer(request):
        
        #collect of data from form submit form
        #request.POST.get('key')
        postData = request.POST
        firstName = postData.get('firstname')
        lastName = postData.get('lastname')
        phone = postData.get('phonenumber')
        email = postData.get('email')
        password = postData.get('password')

        #hold the data of some input field so that user don't need to specify again
        value = {
            'firstName': firstName,
            'lastName': lastName,
            'phone': phone,
            'email': email,
        }
        #create customer message
        customer = Customer(
            firstName=firstName,
            lastName=lastName,
            phone=phone,
            email=email,
            password=password)

        #validation -check for any validation error for the new customer
        error_message = {}
        error_message=validateCustomer(customer)
        

        #saving
        #finally create an object which validate all the fields and 

        if not error_message:
            #hashing the user password before register the password
            customer.password=make_password(customer.password)
            customer.register()

        
        else:
            data= {
                'value': value,
                'error':error_message
            }
            return render(request,'signup.html',data)
        
        return redirect('homepage')
    




def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        #post method..then we get user information and we  need to register them in the database so call the register customer method
        return registerCustomer(request)  




#class based view            
class Login(View):
    #define get method for the login
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        #we submit the login form in which two fields are there email and password and after submit Login Post method is called and from this post method we fetch the value from the submitte section
        email = request.POST.get('email')
        #password send by the user
        password = request.POST.get('password')
        #check if customer exist or not
        customer = Customer.getCustomerByEmail(email)
        error_message=None
        if customer:
            #check customer
            temp = check_password(password, customer.password)
            if temp:
                return redirect('homepage')
            else:
                error_message='Wrong email or password'
        else:
            error_message='Wrong email or password'
        return render(request,'login.html',{'error':error_message}) 
        
        
