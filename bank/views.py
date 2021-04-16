from django.shortcuts import render, redirect
from .models import Account, Transaction
from django.contrib import messages
import datetime


def index(request):
    return render(request, 'bank/index.html')


def create_account(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        amount = request.POST.get('amount', '')
        create = Account(name=name, email=email, balance=amount, Date_of_Creation=datetime.date.today())
        create.save()
        messages.success(request, "Congrats Account Created Successfully")
        return redirect("/bank/view/")
    return render(request, 'bank/create_account.html')


#Account.objects.all()
#Account.objects.get(pk=sender)


def transfer_money(request):
    account = Account.objects.raw('select * from bank_account')
    params = {"account": account}

    if request.method == "POST":
        sender = request.POST.get("sender")
        receiver = request.POST.get("receiver")
        amount = request.POST.get("amount")
        status = False

        if sender != 0 and receiver != 0:
            p = Account.objects.get(pk=sender)
            q = Account.objects.get(pk=receiver)
            if p.balance > int(amount):
                p.balance = int(p.balance) - int(amount)
                q.balance = int(q.balance) + int(amount)
                p.save()
                q.save()
                status = True
                t = Transaction(from_account=p.name, to_account=q.name, amount=amount, status=status,
                                date=datetime.date)
                t.save()
                messages.success(request, "CONGRATULATIONS TRANSACTION SUCCESSFUL")
                return redirect("/bank/transaction_history/")

            else:
                t = Transaction(from_account=p.name, to_account=q.name, amount=amount, status=status,
                                date=datetime.date)
                t.save()
                messages.warning(request, 'TRANSACTION UNSUCCESSFUL due to insufficient balance')
                return redirect("/bank/transaction_history/")

    return render(request, "bank/transfer_money.html", params)


def transfer(request, x):
    x = Account.objects.get(id=x)
    account = Account.objects.all().order_by('id')
    params = {"account": account, "x": x}
    return render(request, 'bank/transfer_money.html', params)


def transaction_history(request):
    trans = Transaction.objects.all().order_by('-T_id')
    params = {"trans": trans}
    return render(request, 'bank/transaction_history.html', params)


def view(request):
    account = Account.objects.all()
    n = len(account)
    if request.method == "POST":
        x = request.POST.get("transfer")
        return redirect("/bank/transfer/" + x)
    params = {"no_of_accounts": n, "range": range(1, n), "account": account}
    return render(request, "bank/view.html", params)
