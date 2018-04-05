from django import forms
from .models import Empleado

class EmpleadoRegModelForm(forms.ModelForm):
	class Meta:
		model = Empleado
		fields = ['username','first_name','last_name']