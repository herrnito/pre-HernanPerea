from django import forms
from .models import Cliente, Tortas, Pedido

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"

class TortasForm(forms.ModelForm):
    class Meta:
        model = Tortas
        fields = "__all__"

class PedidoForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(
        queryset=Cliente.objects.all(), empty_label="Seleccione un cliente"
    )
    servicio = forms.ModelChoiceField(
        queryset=Tortas.objects.filter(disponible=True),
        empty_label="Seleccione una torta"
    )
    class Meta:
        model = Pedido
        fields = "__all__"
        widgets = {"fecha_entrega" : forms.DateTimeInput(attrs={"type" : "datetime-local"})}