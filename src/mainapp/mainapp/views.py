from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from accounts.forms import AccountForm
from accounts.models import Account, Transaction


# Create your views here.
def home(request):
    accounts = Account.objects.all()
    return render(request, "index.html", {'accounts': accounts})

def balanceSheet(request, pk):
    pk = int(pk)
    account = get_object_or_404(Account, pk=pk)
    transactions = Transaction.objects.filter(account_id=pk)
    # accountTransactions = Account.objects.filter(pk=pk)
    # # transactions = get_object_or_404(Transaction, account=pk)
    # for entry in accountTransactions:
    #     transactions = entry.transaction.all()
    #
    # def get_queryset(self):
    #     pk = self.kwargs['pk']
    #     return Transaction.objects.filter(account=pk)



    return render(request, "BalanceSheet.html", {'account': account, 'transactions':transactions})

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


    return render(request, "CreateNewAccount.html", {'accounts': accounts})

def newTransaction(request):
    accounts = Account.objects.all()
    return render(request, "AddTransaction.html", {'accounts': accounts})