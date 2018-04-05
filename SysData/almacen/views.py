from django.shortcuts import render

from .forms import EmpleadoRegModelForm
# Create your views here.


def panel(request):
	titulo = "Panel"
	context = {
		'titulo': titulo, 
	}
	return render(request, 'panel.html', context) 


def registrarEmpleado(request):
	titulo = "Almacen"
	form = EmpleadoRegModelForm(request.POST or None)
	context = {
		'titulo': titulo, 
		'form': form,
	}
	return render(request, 'regEmpleado.html', context)
