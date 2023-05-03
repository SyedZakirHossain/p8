from django.shortcuts import render
from .models import  topic,Contact,btopic,spl,bspl

from django.shortcuts import render,redirect


from django.contrib import messages
from django.http import FileResponse
import io
from django.contrib.auth.models import User,auth
# Create your views here.
def home(request):
    return render(request,'home.html') 

def vspl(request):
     sp = spl.objects.all()
     context = { }
     return render(request,'spl.html',{'sp':sp}) 

def vbspl(request):
     bsp = bspl.objects.all()
     context = { }
     return render(request,'bspl.html',{'bsp':bsp}) 
    
def bhome(request):
    return render(request,'bhome.html') 

def ehome(request):
    return render(request,'ehome.html') 

def contact(request):
    return render(request,'contact.html') 
#========================================================= 
#@login_required(login_url="/login")
def contact(request):
    return render(request, "contact.html")
#========================================================= 

#@login_required(login_url="/login")
def contactsave(request):
    try:
        if request.method == "POST":
            name = request.POST["name"]
            email = request.POST["email"]
            desc = request.POST["desc"]
            values = Contact(name=name, email=email, desc=desc)
            values.save()
            messages.info(request, "Your message is saved and added to database. ")
            messages.info(request, "")
    except:
        pass
    return redirect("/contact")

#========================================================= 
def log(request):
    return render(request,'login.html')

def about(request):
    return render(request,'about.html')

def qr(request):
     tp = topic.objects.all().order_by('tname')
     context = { }
     return render(request,'quran.html',{'top':tp}) 

def bqr(request):
     btp = btopic.objects.all().order_by('btname')
     context = { }
     return render(request,'bquran.html',{'top':btp})       

def tl(request):
     tp = topic.objects.all()
     return render(request,'Topic_List.html',{'top':tp}) 
def btl(request):
     btp = btopic.objects.all()
     return render(request,'bTopic_List.html',{'top':btp}) 
 


def btl1(request):
     btp = btopic.objects.all().filter(btname='অশ্লীলকার্য')
     btname='অশ্লীলকার্য'
     return render(request,'btl1.html',{'top':btp, 'btname':btname})

def btl2(request):
     btp = btopic.objects.all().filter(btname='অসমান')
     btname='অসমান'
     return render(request,'btl1.html',{'top':btp, 'btname':btname})

def btl3(request):
     btp = btopic.objects.all().filter(btname='অলি-মুর্শিদ')
     btname='অলি-মুর্শিদ' 
     return render(request,'btl1.html',{'top':btp, 'btname':btname})


def tl1(request):
     tp = topic.objects.all().filter(tname='Abraham')
     tname='Abraham'
     return render(request,'tl1.html',{'top':tp,'tname':tname}) 

def tl2(request):
     tp = topic.objects.all().filter(tname='Lahab')
     tname='Lahab'
     return render(request,'tl1.html',{'top':tp,'tname':tname}) 

def tl3(request):
     tp = topic.objects.all().filter(tname='Ahad')
     tname='Ahad'
     return render(request,'tl1.html',{'top':tp,'tname':tname}) 

def tl4(request):
     tp = topic.objects.all().filter(tname='Indecencies')
     tname='Indecencies'
     return render(request,'tl1.html',{'top':tp,'tname':tname}) 

def tl5(request):
     tp = topic.objects.all().filter(tname='Do and don\'t')
     tname='Do and don\'t'
     return render(request,'tl1.html',{'top':tp,'tname':tname}) 

def tl6(request):
     tp = topic.objects.all().filter(tname='Notequal')
     tname = 'Not equal'
     return render(request,'tl1.html',{'top':tp, 'tname':tname}) 

def tl7(request):
     tp = topic.objects.all().filter(tname='Oli and Murshid')
     tname = 'Oli and Murshid'
     return render(request,'tl1.html',{'top':tp, 'tname':tname}) 




 
