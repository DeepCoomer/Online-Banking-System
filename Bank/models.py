from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=122,null=True,)
    email = models.CharField(max_length=122,null=True,)
    phoneno = models.CharField(max_length=10,null=True,)
    Report = models.CharField(max_length=122,null=True,)
    objects = models.Manager()

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    Name = models.CharField(max_length=122,null=True,blank=True)
    AccountNo = models.CharField(max_length=7,null=True,blank=True)
    Email = models.CharField(max_length=122,null=True,blank=True)
    AccountType = models.CharField(max_length=122,null=True,blank=True)
    CurrentBalance = models.IntegerField(null=True,blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.AccountNo

class Bank_statement(models.Model):
    Name = models.CharField(max_length=122,null=True,blank=True)
    AccountNo = models.CharField(max_length=7,null=True,blank=True)
    Date = models.DateTimeField(max_length=7,null=True,blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.Name
    
class Transfer_money(models.Model):
    SenderName = models.CharField(max_length=122,null=True,blank=True)
    SenderAccountNo = models.CharField(max_length=7,null=True,blank=True)
    RecieverName = models.CharField(max_length=122,null=True,blank=True)
    RecieverAccountNo = models.CharField(max_length=7,null=True,blank=True)
    Amount = models.IntegerField(null=True,blank=True)
    Date = models.DateTimeField(null=True,blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.SenderName
        