from django.shortcuts import render
from django.utils.timezone import now, timedelta
from django.db.models import Count
from datetime import timedelta


# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Chicken, Egg
from .forms import ChickenForm, EggForm
from django.utils import timezone
from django.db.models import Sum

# Chicken Views
def chicken_list(request):
    chickens = Chicken.objects.all()
    return render(request, 'inventory/chicken_list.html', {'chickens': chickens})

def chicken_add(request):
    if request.method == 'POST':
        form = ChickenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chicken_list')
    else:
        form = ChickenForm()
    return render(request, 'inventory/chicken_form.html', {'form': form})

def chicken_edit(request, pk):
    chicken = get_object_or_404(Chicken, pk=pk)
    if request.method == 'POST':
        form = ChickenForm(request.POST, instance=chicken)
        if form.is_valid():
            form.save()
            return redirect('chicken_list')
    else:
        form = ChickenForm(instance=chicken)
    return render(request, 'inventory/chicken_form.html', {'form': form})

def chicken_delete(request, pk):
    chicken = get_object_or_404(Chicken, pk=pk)
    chicken.delete()
    return redirect('chicken_list')

# Egg Views
def egg_list(request):
    eggs = Egg.objects.all()
    return render(request, 'inventory/egg_list.html', {'eggs': eggs})

def egg_add(request, chicken_id):
    chicken = get_object_or_404(Chicken, pk=chicken_id)
    if request.method == 'POST':
        form = EggForm(request.POST)
        if form.is_valid():
            egg = form.save(commit=False)
            egg.chicken = chicken
            egg.save()
            return redirect('egg_list')
    else:
        form = EggForm()
    return render(request, 'inventory/egg_form.html', {'form': form, 'chicken': chicken})

def chickens_by_health_status(request):
    chickens_by_health = Chicken.objects.values('health_status').annotate(count=Count('id'))
    return render(request, 'inventory/chickens_by_health.html', {'chickens_by_health': chickens_by_health})

def total_eggs_for_chicken(request, chicken_id):
    chicken = get_object_or_404(Chicken, pk=chicken_id)
    total_eggs = Egg.objects.filter(chicken=chicken).aggregate(Sum('quantity'))['quantity__sum'] or 0
    return render(request, 'inventory/total_eggs_for_chicken.html', {'chicken': chicken, 'total_eggs': total_eggs})

def total_eggs_last_7_days(request):
    last_7_days = timezone.now() - timedelta(days=7)
    total_eggs = Egg.objects.filter(date_collected__gte=last_7_days).aggregate(Sum('quantity'))['quantity__sum'] or 0
    return render(request, 'inventory/total_eggs_last_7_days.html', {'total_eggs': total_eggs})