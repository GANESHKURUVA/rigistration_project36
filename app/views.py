from django.shortcuts import render
from app.forms import *

from django.http import HttpResponse
# Create your views here.


def Rigistration(request):
    RFO=RigistrationForm()
    d={'RFO':RFO}
    if request.method=='POST':
        RFOD=RigistrationForm(request.POST)
        if RFOD.is_valid():
            return HttpResponse(str(RFOD.cleaned_data))
        else:
            return HttpResponse('invalid data entered')

    return render(request,'rigistration.html',d)