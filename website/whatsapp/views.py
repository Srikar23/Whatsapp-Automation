from django.shortcuts import render
from . import message, fileSending


# Create your views here.
def home(request):
    return render(request, 'index.html')

def send_Message(request):
    return render(request, 'send.html')

def send_File(request):
    return render(request, 'file.html')

def mssg(request):
    recipient_Name = request.GET['contact name']
    msg = request.GET['Message']
    time_In_Secs = int(request.GET['Time'])
    message.msg(recipient_Name, msg, time_In_Secs)
    return render(request, 'send.html')

def file(request):
    recipient_Name = request.GET['contact name']
    path = request.GET['file']
    time_In_Secs = int(request.GET['Time'])
    fileSending.file(recipient_Name, path, time_In_Secs)
    return render(request, 'file.html')