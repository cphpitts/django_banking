from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from accounts.forms import AccountForm, TransactionForm
from accounts.models import Account, Transaction
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def home(request):
    accounts = Account.objects.all()
    return render(request, "index.html", {'accounts': accounts})

def balanceSheet(request, pk):
    pk = int(pk)
    account_info = get_object_or_404(Account, pk=pk)
    account = Account.objects.filter(pk=pk)
    transactions = Transaction.objects.filter(account__account_Num=account)

    return render(request, "BalanceSheet.html", {'account': account, 'transactions':transactions, 'accountInfo': account_info})

def addAccount(request):
    form = AccountForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        print(form.errors)
        form = AccountForm()
        context = {
            'form': form
        }
    return render(request, 'CreateNewAccount.html', context)

def newTransaction(request):
    form = TransactionForm(request.POST or None)
    if form.is_valid():
        newForm = form.save(commit=False)
        logger.error(newForm.account)
        account = Account.objects.get(account_Num = newForm.account.account_Num)

        account.balance = int(account.balance - form.cleaned_data['amount'])
        newForm.current_balance = account.balance


        newForm.save()

        account.save()
        return redirect('home')
    else:
        print(form.errors)
        form = TransactionForm()
        context = {
            'form': form
        }
    return render(request, 'AddTransaction.html', context)