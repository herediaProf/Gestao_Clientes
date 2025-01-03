from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from  django.urls import reverse
from .models import Person
from .forms import PersonForm

# Create your views here.

@login_required
def persons_list(request):
    # ler as pessoas do Banco
    persons = Person.objects.all()
    return render(request, 'person.html', {'persons': persons})
    return render(request, 'persons_list.html', {'persons': persons})


@login_required
def persons_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        form.save()
        return redirect('persons_list')    
    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)
    
    if form.is_valid():
        form.save()
        return redirect('persons_list')
    
    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)
   
    if request.method == 'POST':
        person.delete()
        return redirect('persons_list')
    return render(request, 'persons_delete_confirm.html', {'person': person})
    
    




    
