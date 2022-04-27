from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

import requests

from .util import _url, _header, get_data, get_variable

from .forms import TipoDeCambioForm
from .models import TipoDeCambio


# SHOW
@login_required()
def show(request):
    tdcs = TipoDeCambio.objects.all()
    table = ""
    for tipo in tdcs:
        table += tipo.to_row()

    context = {
        'tipos_de_cambio': table
    }
    return render(request, 'show.html', context=context)

# ADD
@login_required()
def add(request):

    get_form = TipoDeCambioForm(request.POST or None)

    if get_form.is_valid():
        fecha = get_form.cleaned_data.get('fecha')
        data = get_data(fecha.strftime("%d/%m/%Y"))
        response = requests.post(url=_url, headers=_header, data=data)
        venta = get_variable(response.text, "venta")
        compra = get_variable(response.text, "compra")
        
        new_tdc = TipoDeCambio()
        new_tdc.fecha = fecha
        new_tdc.venta = venta
        new_tdc.compra = compra
        if venta!='' and compra!='':
            new_tdc.save() 

        return redirect('/show')
    context = {
        'form': get_form
    }
    return render(request, 'add.html', context=context)

# UPDATE
@login_required()
def update(request, id):
    tdc = TipoDeCambio.objects.get(id=id)
    if request.method == 'POST':
        get_form = TipoDeCambioForm(request.POST, instance=tdc)
        if get_form.is_valid():
            fecha = get_form.cleaned_data.get('fecha')
            data = get_data(fecha.strftime("%d/%m/%Y"))
            response = requests.post(url=_url, headers=_header, data=data)
            venta = get_variable(response.text, "venta")
            compra = get_variable(response.text, "compra")
            
            tdc.fecha = fecha
            tdc.venta = venta
            tdc.compra = compra
            if venta!='' and compra!='':
                tdc.save() 
            
        return redirect('/show')
    else:
        get_form = TipoDeCambioForm(instance=tdc)
    return render(request, "edit.html", {'form': get_form, 'tdc': tdc})

# DELETE
@login_required()
def delete(request, id):
    if not request.user.is_authenticated:
        return redirect('/login')

    tdc = TipoDeCambio.objects.get(id=id)
    tdc.delete()
    return redirect('/show')

