from django.views import View
from django.shortcuts import render, redirect

from store.models.customer import Customer
from django.contrib.auth.hashers import make_password



class Signup(View):

    def validateCustomer(self, customer):
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
    

    def get(self, request):
        return render(request, 'signup.html')
    def post(self, request):
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
        error_message=self.validateCustomer(customer)
        

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
    
 