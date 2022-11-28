
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .conect_belvo import ConectBelvo


from datetime import date, datetime, timedelta

def index(request):
    client = ConectBelvo()
    all_institutions = client.all_institutions()
    # for institution in all_institutions:
    #     print(institution["icon_logo"])

    context = {"institutions":all_institutions}
    
    return render(request, 'centralis/index.html', context)


def conect(request, id):
    client = ConectBelvo()
    institution = client.get_intitution(institution_id=id)
    context = {'institution': institution}
    
    return render(request, 'centralis/conect.html', context)


def connect_account(request):
    if request.method == "POST":
        context = {'has_error': False, 'data':request.POST}
        id = request.POST.get('id')
        username = request.POST.get('username')
        password = request.POST.get('password')
        institution = request.POST.get('institution')
        if len(password)<8:
            messages.add_message(request, messages.ERROR, "Password should be at least 8 characters") 
            context['has_error'] = True
        if not username:
            messages.add_message(request, messages.ERROR, "Username is requered") 
            context['has_error'] = True
        
        if context['has_error']:
            return HttpResponseRedirect(reverse("conect", kwargs={'id':id}))
        
        if not context['has_error']:
            client = ConectBelvo()
            link = client.create_links(institution=institution,username=username,password=password)
            
            if not "id" in link:
                error = link[0]["message"]
                print(error)
                messages.add_message(request, messages.ERROR, error) 
                return HttpResponseRedirect(reverse("conect", kwargs={'id':id}))

            else:
                context['link'] = link
            
            messages.add_message(request, messages.SUCCESS, "Entidad enlazada con éxito! Puedes registrarte para mas opciones") 
            return HttpResponseRedirect(reverse("transactions", kwargs={'id':link['id']}))
        
    return render(request, 'centralis/conect.html')


def transactions_account(request, id):
    client = ConectBelvo()
    transactions = client.all_transactions(link=id)
    response = []
    reg=0
    for transaction in transactions:
        response.append({
            "id":transaction['id'],
            "type":transaction['type'],
            'status': transaction['status'],
            'amount': transaction['amount'],
            'date': transaction['created_at'],
            'reference': transaction['reference'],
            'description': transaction['description'],
            'merchant': transaction['merchant']['name'],
        }) 
        reg+=1
        if reg == 20:
            break
    if not response:
        return HttpResponseRedirect(reverse("transactions", kwargs={'id':id}))
        
    context = {'transactions': response}
    return render(request, 'centralis/transactions.html', context)
