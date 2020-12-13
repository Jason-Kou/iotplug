from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import requests
from django.views.decorators.csrf import csrf_exempt
from iotplug.control import control_plug

# Create your views here.

def qr(request):
    # Render the index page.
    print("so......slow")
    return render(request, "qrcode.html")

@csrf_exempt
def control(request):
    print(request.POST)
    if "on_button" in request.POST:
        print("on........")
        control_plug("turn_on")
    elif "off_button" in request.POST:
        print("off..........")
        control_plug("turn_off")
    # print(feedback)
    return render(request, "control.html")