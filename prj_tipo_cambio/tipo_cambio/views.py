from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from .forms import TipoDeCambioForm
from .models import TipoDeCambio


# SHOW
@login_required()
def show(request):
    # if not request.user.is_authenticated:
    #     return redirect('/login')

    tdcs = TipoDeCambio.objects.all()
    table = ""
    for tipo in tdcs:
        table += tipo.to_row()

    print(table)
    context = {
        'tipos_de_cambio': table
    }
    return render(request, 'show.html', context=context)

# ADD
def add(request):
    if not request.user.is_authenticated:
        return redirect('/login')

    get_form = TipoDeCambioForm(request.POST or None)
    if get_form.is_valid():
        get_form.save()
        return redirect('/show')
    context = {
        'form': get_form
    }
    return render(request, 'add.html', context=context)

# UPDATE
def update(request, id):
    if not request.user.is_authenticated:
        return redirect('/login')

    tdc = TipoDeCambio.objects.get(id=id)
    if request.method == 'POST':
        form = TipoDeCambioForm(request.POST, instance=tdc)
        if form.is_valid():
            form.save()
            return redirect('/show')
    else:
        form = TipoDeCambioForm(instance=tdc)
    return render(request, "edit.html", {'form': form, 'tdc': tdc})

# DELETE
def delete(request, id):
    if not request.user.is_authenticated:
        return redirect('/login')

    tdc = TipoDeCambio.objects.get(id=id)
    tdc.delete()
    return redirect('/show')

