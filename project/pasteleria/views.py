from django.shortcuts import render, redirect
from .models import Cliente, Tortas, Pedido
from .forms import ClienteForm, TortasForm, PedidoForm

# Create your views here.
def index(request):
    return render(request, 'pasteleria/index.html')

def cliente_list(request):
    query =  Cliente.objects.all()
    context = {"objetc_list": query}
    return render(request, "pasteleria/cliente_list.html", context)
  
def tortas_list(request):
    query =  Tortas.objects.all()
    context = {"objetc_list": query}
    return render(request, "pasteleria/tortas_list.html", context)

def pedido_list(request):
    query =  Pedido.objects.all()
    context = {"objetc_list": query}
    return render(request, "pasteleria/pedido_list.html", context)

def cliente_create(request):
    if request.method == "GET":
        form = ClienteForm()
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente_list")
    return render(request, "pasteleria/cliente_create.html", {'form': form})

def torta_create(request):
    if request.method == "GET":
        form = TortasForm()
    if request.method == "POST":
        form = TortasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("torta_list")
    return render(request, "pasteleria/torta_create.html", {'form': form})

def pedido_create(request):
    if request.method == "GET":
        form = PedidoForm()
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("pedido_list")
    return render(request, "pasteleria/pedido_create.html", {'form': form})

