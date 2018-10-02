from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models

# Create your views here.
def index(request):
   return render(request,'index.html')

######################################################3
def require_login(request):
   return render(request,'login.html')

def login(request):
   username=request.POST.get('username','')
   password=request.POST.get('password','')
   rt=models.validate_login(username,password)
   if rt == True:
      return HttpResponseRedirect('/login_success/?username='+username)
   else:
      context={'error': 'user name or password is wrong','username': username, 'password': password}
      return render(request,'login.html/',context)

def login_success(request):
   username=request.GET.get('username','')
   return render(request,'list.html/',{'username': username, 'pics': models.pics})
   #return HttpResponse('</html><body><h3 style="color:green;">'+username+', you just logged in successfully </h3></br></br></br> <button onclick="window.location.href=\'/require_login/\'">Logout</button></body></html>')
######################################################3
def require_register(request):
   return render(request,'register.html')

def register(request):
   username=request.POST.get('username','')
   email=request.POST.get('email','')
   password=request.POST.get('password','')
   password2=request.POST.get('password2','')
   rt,mesg=models.validate_register(username,email,password,password2)
   if rt == True:
      return HttpResponseRedirect('/register_success/?username='+username)
   else:
      context={'error': mesg,'username': username, 'email': email}
      return render(request,'register.html/',context)

def register_success(request):
   username=request.GET.get('username','')
   return HttpResponse('</html><body><h3 style="color:green;" id="messageid" name="message">'+username+', you just registered successfully </h3></br></br></br> <button onclick="window.location.href=\'/\'" id="homeid" name="homebtn">Home</button></body></html>')
######################################################3
def under_construction(request):
   username=request.GET.get('username','')
   return HttpResponse('</html><body><h1 style="color:blue;">Under Construction</h1></br></br></br><button onclick="window.location.href=\'/\'">Home</button></body></html></body></html>')
######################################################3
