from django.shortcuts import render

# Create your views here.
def usdf(request):
    d={'data':'HAI MADHU U CAN DO THIS'}
    return render(request,'usdf.html',d)