from django.shortcuts import render

# newapp views here
def index(request):
    return render(request, "newapp/index.html")
    
