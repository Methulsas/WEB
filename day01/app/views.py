from django.shortcuts import render
from .models import*
from .forms import *
from django.core.paginator import Paginator
from .filters import *




# Create your views here.
def category_view(request):
    page_number = request.GET.get('page')
    filter = categoryFilter(request.GET, queryset=category.objects.all())
    categories = filter.qs
    
    paginator = Paginator(categories, 3) 
    page = paginator.get_page(page_number)
    
    if request.method == 'POST':
        form = categoryFrom(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = categoryFrom()
    context = {'form':form, 'page':page}
    return render(request, 'Category.html',context)


def unit_view(request):
    units = unit.objects.all()
    if request.method == 'POST':
        form = unitFrom(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = unitFrom()
    context = {'form':form, 'uts':units}
    return render(request, 'unit.html',context)      
    

def item_view(request):
    page_number = request.GET.get('page')
    filter = itemFilter(request.GET, queryset=item.objects.all())
    items = filter.qs
    
    paginator = Paginator(items, 3) 
    page = paginator.page(page_number)
    if request.method == 'POST':
        form = itemForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = itemForm()
    context = {'form':form, 'page':page}
    return render(request, 'item.html',context)

def Supplier_view(request):
    Suppliers = Supplier.objects.all()
    if request.method == 'POST':
        form = SupplierFrom(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SupplierFrom()
    context = {'form':form, 'supplrs':Suppliers}
    return render(request, 'Supplier.html',context)  

def order_view(request):
    orders = order.objects.all()
    if request.method == 'POST':
        form = orderFrom(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = orderFrom()
    context = {'form':form, 'ordrs':orders}
    return render(request, 'order.html',context)  

def employee_view(request):
    employees = Employee.objects.all()
    if request.method == 'POST':
        form = EmployeeFrom(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EmployeeFrom()
    context = {'form':form, 'employs':employees}
    return render(request, 'employee.html',context) 