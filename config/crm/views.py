from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.
from .forms import ClientForm, OrderForm, ServiceForm, EditOrderForm
from .models import Clients, Orders, Service, Department, ProjectService, User


def index(request):
    return render(request, 'index.html')


def clients(request):
    clients = Clients.objects.all()
    form = ClientForm(request.POST)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('clients')
    return render(request, 'clients.html',
                  {'klients': clients,
                   "form": form,
                   'klients_count': Clients.objects.count(),
                   })


def edit_client(request, pk):
    client = Clients.objects.get(id=pk)
    form = ClientForm(request.POST or None, instance=client)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('clients')
    return render(request, 'edit_client.html',
                  {'form': form,
                   'pk': pk,
                   'client': client, })


def offic(request):
    services = Service.objects.filter(Q(parent__isnull=False))
    # order_archive = Orders.objects.filter(pk=pk, is_archive=False)
    orders = Orders.objects.filter(user=request.user)
    departments = Department.objects.all()
    form = OrderForm(request.POST)
    if form.is_valid() and request.method == 'POST':
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()

        for i in request.POST.getlist('service'):
            services = Service.objects.filter(parent=i)

            for service in services:
                project_service = ProjectService()
                project_service.order = instance
                project_service.service = service
                project_service.parcent = 0
                project_service.max_parcent = 0
                project_service.save()

        return redirect('offic')
    return render(request, 'ofis.html',
                  {'orders': orders,
                   'departments': departments,
                   'form': form,
                   'order_count': Orders.objects.count(),
                   'services': services
                   })


def edit_offic(request, pk):
    order = Orders.objects.get(id=pk)
    form = EditOrderForm(request.POST or None, instance=order)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('offic')
    return render(request, 'edit_offic.html',
                  {'order': order,
                   'form': form})


def service(request):
    services = Service.objects.all()
    form = ServiceForm(request.POST)
    if form.is_valid() and request.method == 'POST':
        instance = form.save(commit=False)
        instance.type = request.POST.get('parent')
        instance.save()
        return redirect('service')
    return render(request, 'spravitcik.html',
                  {'form': form,
                   'services': services})


def archive(request, pk):
    Orders.objects.filter(pk=pk).update(is_archive=True)
    return render(request, 'ofis.html')


def department(request, pk):
    orders = Orders.objects.get(pk=pk)
    projectservices = ProjectService.objects.filter(order=orders)
    result_parcent = 0
    reuslt_sum = 0
    sum_percent = 0
    max_percent_sum = 0
    for item in projectservices:
        result_parcent += item.parcent
        reuslt_sum += item.total_prince()
        max_percent_sum += item.max_parcent
        sum_percent += (item.parcent * item.max_parcent) / 100
    return render(request, 'department.html',
                  {'orders': orders,
                   'projectservices': projectservices,
                   'result_parcent': result_parcent,
                   'reuslt_sum': reuslt_sum,
                   'sum_percent': sum_percent,
                   'max_percent_sum': max_percent_sum,
                   'result': reuslt_sum * max_percent_sum / 100
                   })


# def edit_department(request, pk):
#     return render(request, 'edit_department.html', {})


def login_user(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('home')
    return render(request, 'sign_in.html', {'form': form})


def sign_out(request):
    logout(request)
    return redirect('login_user')


def edit_percent(request, pk):
    project_service = ProjectService.objects.get(pk=pk)
    project_service.parcent = request.POST['percent']
    project_service.max_parcent = request.POST['max_parcent']
    project_service.save()
    return redirect('offic')
