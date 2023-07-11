from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Stock, Items, Casing, Production
from .forms import InventoryForm, EditForm, CasingForm, THTForm,  MyForm
from django.contrib.auth.models import User
from user.models import Profile
# Create your views here.

@login_required
def index(request):
    items = Production.objects.all()
    if request.method == 'POST' :
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MyForm()

    
    context = {
        'items' : items,
        'form' : form,
    }
    return render(request,'dashboard/index.html', context)

@login_required
def staff(request):
    items = Profile.objects.select_related('user')
    # profile_items = Profile.objects.all()
    # user_items = User.objects.all()
    context = {
        'items' : items
    }
    return render(request,'dashboard/staff.html',context)

@login_required
def reports(request):
    items = Profile.objects.select_related('user')
    context = {
        'items' : items
    }
    return render(request,'dashboard/reports.html',context)


@login_required
def products(request):
    items = Stock.objects.all()
    if request.method == 'POST' :
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = InventoryForm()

    
    context = {
        'items' : items,
        'form' : form,
    }
    return render(request,'dashboard/products.html', context)

@login_required
def metadata(request):
    return render(request,'dashboard/metadata.html')

@login_required
def edit_inventory(request,pk):
    item = Stock.objects.get(id=pk)
    if request.method == 'POST':
        form = EditForm(request.POST)
    else:
        form = EditForm()
    context = {
        'form' : form,
        'item' : item
    }
    return render(request,'dashboard/edit_inventory.html',context)
#production processes

@login_required
def casing(request):
    items = Casing.objects.all()
    if request.method == 'POST' :
        form = CasingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('casing')
    else:
        form = CasingForm()

    context = {
        'items' : items,
        'form' : form,
    }
    return render(request,'dashboard/casing.html', context)


@login_required
def phase1_tht(request):
    phase = "THT"
    items = Production.objects.raw('SELECT * FROM dashboard_production WHERE phase = %s',[phase])
    #items = Production.objects.all()
    if request.method == 'POST' :
        form = THTForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('phase1_tht')
    else:
        form = THTForm()

    context = {
        'items' : items,
        'form' : form,
    }
    return render(request,'dashboard/phase1_tht.html', context)

@login_required
def phase2_smt(request):
    phase = "SMT"
    items = Production.objects.raw('SELECT * FROM dashboard_production WHERE phase = %s',[phase])
    #items = Production.objects.all()
    if request.method == 'POST' :
        form = THTForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('phase2_smt')
    else:
        form = THTForm()

    context = {
        'items' : items,
        'form' : form,
    }
    return render(request,'dashboard/phase2_smt.html', context)

@login_required
def phase3_tunning(request):
    phase = "tunning"
    items = Production.objects.raw('SELECT * FROM dashboard_production WHERE phase = %s',[phase])
    # items = Production.objects.all()
    if request.method == 'POST' :
        form = THTForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('phase3_tunning')
    else:
        form = THTForm()

    context = {
        'items' : items,
        'form' : form,
    }
    return render(request,'dashboard/phase3_tunning.html', context)

@login_required
def monitor_assembly(request):
    phase = "monitor assembly"
    items = Production.objects.raw('SELECT * FROM dashboard_production WHERE phase = %s',[phase])
    # items = Production.objects.all()
    if request.method == 'POST' :
        form = THTForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('monitor_assembly')
    else:
        form = THTForm()

    context = {
        'items' : items,
        'form' : form,
    }
    return render(request,'dashboard/monitor_assembly.html', context)

@login_required
def communication_config(request):
    phase = "communication config"
    items = Production.objects.raw('SELECT * FROM dashboard_production WHERE phase = %s',[phase])
    # items = Production.objects.all()
    if request.method == 'POST' :
        form = THTForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('communication_config')
    else:
        form = THTForm()

    context = {
        'items' : items,
        'form' : form,
    }
    return render(request,'dashboard/communication_config.html', context)

@login_required
def analysis(request):
    phase = "analysis"
    items = Production.objects.raw('SELECT * FROM dashboard_production WHERE phase = %s',[phase])
    # items = Production.objects.all()
    if request.method == 'POST' :
        form = THTForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('analysis')
    else:
        form = THTForm()

    context = {
        'items' : items,
        'form' : form,
    }
    return render(request,'dashboard/analysis.html', context)

@login_required
def correction(request):
    phase = "correction"
    items = Production.objects.raw('SELECT * FROM dashboard_production WHERE phase = %s',[phase])
    # items = Production.objects.all()
    if request.method == 'POST' :
        form = THTForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('correction')
    else:
        form = THTForm()

    context = {
        'items' : items,
        'form' : form,
    }
    return render(request,'dashboard/correction.html', context)

@login_required
def phases(request, option):
    context = {'option': option}
    return render(request, 'phases.html', context)
