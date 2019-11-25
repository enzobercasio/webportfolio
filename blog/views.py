from django.shortcuts import render

# Create your views here.
def myblogs (request):
    return render(request,'blog/myblogs.html')