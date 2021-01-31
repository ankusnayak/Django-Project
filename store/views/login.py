from django.views import View
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.shortcuts import render,redirect



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
