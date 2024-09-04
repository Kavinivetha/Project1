from django.shortcuts import render
from django.http import HttpResponse
from .models import docusers,sendmessage


# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def bookappointment(request):
   # print(request.POST)     
    name=request.POST['name']
    email=request.POST['email']
    mobile=request.POST['mobile']
    doctor=request.POST['doctor']
    date=request.POST['date']
    time=request.POST['time']
    reason=request.POST['reason']
    count=docusers.count_documents({"mobile":mobile})

    if count==0:
        data={
            "name":name,
            "email":email,
            "mobile":mobile,
            "doctor":doctor,
            "date":date,
            "time":time,
            "reason":reason
        }
        docusers.insert_one(data)
        all_data=docusers.find()
        return render(request,'index.html',{'data':all_data})
    else:
        
        all_data=docusers.find()
        print("You have already booked an appointment")
        return render(request,'confirmed.html',{'data':all_data})

def sendmessages(request):
    name=request.POST['name']
    email=request.POST['email']
    subject=request.POST['subject']
    message=request.POST['message']

    record={
        "name":name,
        "email":email,
        "subject":subject,
        "message":message
    }
    sendmessage.insert_one(record)
    return render(request,'contact.html')
    
def service(request):
    return render(request,'service.html')

def contact(request):
    return render(request,'contact.html')

def feature(request):
    return render(request,'feature.html')

def team(request):
    return render(request,'team.html')
def appointment(request):
    return render(request,'appointment.html')

def testimonial(request):
    return render(request,'testimonial.html')

def error(request):
    return render(request,'404.html')

def confirmed(request):
    return render(request,'confirmed.html')


