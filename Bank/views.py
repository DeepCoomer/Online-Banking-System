from django.shortcuts import render,redirect
from Bank.models import Contact
from Bank.models import Customer
from Bank.models import Bank_statement
from Bank.models import Transfer_money
import datetime
from django.contrib import messages
# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phoneno = request.POST.get('phoneno')
        Report = request.POST.get('Report')
        index = Contact(name=name,email=email,phoneno=phoneno,Report=Report)
        index.save()
    return render(request,'index.html')

def CustomerData(request):
    customer = Customer.objects.all()
    return render(request,'data.html',{'customers':customer})

def bank_statement(request):
    return render(request,'bank_statement.html')

def bank_statement_details(request):
    if request.method == "POST":
        Name = request.POST.get('Name')
        AccountNo = request.POST.get('AccountNo')
        Date = datetime.datetime.now()
        bank_statement_details = Bank_statement(Name=Name,AccountNo=AccountNo,Date=Date)
        bank_statement_details.save()
    bank = Customer.objects.filter(Name=Name,AccountNo=AccountNo)
    return render(request,'bank_statement_details.html',{'bank':bank})

def transfer_money(request):
    if request.method == "POST":
        SenderName = request.POST.get('SenderName')
        SenderAccountNo = request.POST.get('SenderAccountNo')
        RecieverName = request.POST.get('RecieverName')
        RecieverAccountNo = request.POST.get('RecieverAccountNo')
        Amount = int(request.POST.get('Amount'))
        Date = datetime.date.day()
        transfer_money = Transfer_money(SenderName=SenderName,SenderAccountNo=SenderAccountNo,RecieverName=RecieverName,RecieverAccountNo=RecieverAccountNo,Amount=Amount,Date=Date)
        transfer_money.save()
        sender = Customer.objects.filter(Name=SenderName,AccountNo=SenderAccountNo)
        reciever = Customer.objects.filter(Name=RecieverName,AccountNo=RecieverAccountNo)
        for s in sender:
            sbalance = s.CurrentBalance
            semail = s.Email
            saccounttype = s.AccountType 
        for r in reciever:
            rbalance = r.CurrentBalance
            remail = r.Email
            raccounttype = r.AccountType
        t = transfer_money.Amount
        if t>0 and t<sbalance:
            sbalance = sbalance - t
            rbalance = rbalance + t
            sender = Customer.objects.get(AccountNo=SenderAccountNo)
            sender.CurrentBalance = sbalance
            sender.Email = semail
            sender.AccountType = saccounttype    
            sender.save()
            reciever = Customer.objects.get(AccountNo=RecieverAccountNo)
            reciever.CurrentBalance = rbalance
            reciever.Email = remail
            reciever.AccountType = raccounttype
            reciever.save()
            messages.add_message(request,messages.SUCCESS,'Transaction Successful')
        else:
            messages.add_message(request, messages.ERROR, 'Transaction Failed.')
    return render(request,'transfer_money.html')

def transfer_history(request):
    transfer = Transfer_money.objects.all().order_by('-Date')
    return render(request,'transfer_history.html',{'transfer':transfer})