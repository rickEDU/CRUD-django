from django.shortcuts import render, redirect
from .models import Cao
from .form import CaoForm

def list_cao(request):
    caos = Cao.objects.all()
    return render(request, 'canil.html', {'caos': caos})


def create_cao(request):
    form = CaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_cao')

    return render(request, 'CAOs-form.html', {'form': form})


def update_cao(request, id):
    cao = Cao.objects.get(id=id)
    form = CaoForm(request.POST or None, instance=cao)

    if form.is_valid():
        form.save()
        return redirect('list_cao')

    return render(request, 'CAOs-form.html', {'form': form, 'cao': cao})


def delete_cao(request, id):
    cao = Cao.objects.get(id=id)

    if request.method == 'POST':
        cao.delete()
        return redirect('list_cao')

    return render(request, 'delete-confirm.html', {'cao': cao})


