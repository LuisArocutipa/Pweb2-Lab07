from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):

    send_mail('Hello from PrettyPrinted',
    'Hello there. This is an automated message.',
    'larocutipa@unsa.edu.pe',
    ['sasaco5121@iturchia.com'],
    fail_silently=False)
    
    return render(request, 'relaciones/index.html')