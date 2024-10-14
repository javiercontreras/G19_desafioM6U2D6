from django.shortcuts import render

def main(request):
    empleados = ['Empleado1', 'Empleado2', 'Empleado3','Empleado4','Empleado5']
    context = {'empleados': empleados}
    return render(request,'main.html',context)

