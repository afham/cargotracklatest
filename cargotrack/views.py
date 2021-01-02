from django.shortcuts import render
from .models import Destination
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def home(request):

	if request.method=='POST':
		
		movetype=request.POST['movetype']
		
		movedate=request.POST['movedate']
		movefrom=request.POST['movefrom']
		moveto=request.POST['moveto']
		waytorecieve=request.POST['waytorecieve']
		name=request.POST['name']
		email=request.POST['email']
		phone=request.POST['phone']
		other=request.POST['other']

		price=236 
		
		subject=("Dear {} ,\nThank you for contacting CARGOTRACK\n\nAccording to your given details:\n\nMoving from location : {}\nMoving to location : {}\nDATE : {}\nMovetype : {}\nCBM : 36\nWeight : 67kg\n\nThe expected quote price for your shipment is {} SAR".format(name,movefrom,moveto,movedate,movetype,price))
		print(email)
		
		#databse save
		#ins = Destination(name=name,phone=phone,email=email,movetype=movetype,movefrom=movefrom,moveto=moveto,movedate=movedate,waytorecieve=waytorecieve,other=other)
		#ins.save()
		
		print("the data has been recorded in database")

		send_mail("CARGOTRACK QUOTE PRICE FOR YOUR SUBMISSION",subject,settings.EMAIL_HOST_USER,[email,], fail_silently=False)

		return render(request, "home.html",)

	else:
		return render(request, "home.html",)

# Create your views here.

def contact(request):
	context={}
	return render(request, 'contact.html',context)

def about(request):
	context={}
	return render(request, 'about.html',context)

def services(request):
	context={}
	return render(request, 'services.html',context)

def gallery(request):
	context={}
	return render(request, 'gallery.html',context)
