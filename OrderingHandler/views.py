from django.shortcuts import render
from .models import Hall, Table, Order
from django.http import HttpResponse
from django.core.mail import send_mail
import os
 
def index(request):
    hall = Hall.objects.all()[0]
    tables = Table.objects.all()
    orders = Order.objects.all()
    data = {"hall": hall,"tables":tables,'orders':orders}

    if request.method == 'POST':
        table = Table.objects.get(table_id=request.POST.get("tablenumber"))
        date = request.POST.get("date")
        name = request.POST.get("name")
        email = request.POST.get("email")
        Order.objects.create(table=table, date=date,client_name =name,email=email)
        send_mail('Booked table','You booked table {} on {}!'.format(request.POST.get("tablenumber"), date),
        os.getenv('host_mail') , [email], fail_silently=False,)



    return render(request, "home.html", data)