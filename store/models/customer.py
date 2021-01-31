from django.db import models

class Customer(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    

    def register(self):
        self.save()
    def isExists(self):
        #here we filter out the email if the email already exists ..for example we call this method when a new user about to created and compare it with rest of the emails
        if Customer.objects.filter(email=self.email):
            return True
        return False
    
    @staticmethod
    def getCustomerByEmail(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
               
