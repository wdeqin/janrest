from django.shortcuts import render

def index(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html', { 'maillist': [ 'If you like to contact me, email me: ', 'wdeqin@gmail.com' ] })
