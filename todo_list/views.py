from django.shortcuts import render, redirect
from .models import *
from .forms import ListForm
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, ('Item Has Been Added To List!'))
            return render(request, 'home.html', {'all_items': all_items})

    else:
        all_items = List.objects.all
        return render(request, 'home.html', {'all_items': all_items})

def delete(request, List_id):
    item = List.objects.get(pk=List_id)
    item.delete()
    messages.success(request, ('Item Has Been Deleted!'))
    return redirect('home')


def cross_off(request, List_id):
    item = List.objects.get(pk=List_id)
    item.completed = True
    item.save()
    return redirect('home')

def uncross(request, List_id):
    item = List.objects.get(pk=List_id)
    item.completed = False
    item.save()
    return redirect('home')

def edit(request, List_id):
    if request.method == 'POST':
        item = List.objects.get(pk=List_id)
        form = ListForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()

            messages.success(request, ('Item Has Been Edited!'))
            return redirect('home')

    else:
        item = List.objects.get(pk=List_id)
        return render(request, 'edit.html', {'item': item})
