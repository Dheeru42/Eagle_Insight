from django.shortcuts import render,HttpResponse
from Plate.models import Vehicle

# Create your views here.
def index(request):
    return render(request,'index.html')
    # return HttpResponse("info")