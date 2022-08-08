from django.shortcuts import render

# Create your views here.



def Homepage(request):
    return render (request,'Faster/index.html',{})

def Aboutpage(request):
    return render(request,'Faster/about.html',{})

def Servicepage(request):
    return render(request,'Faster/service.html',{})
    
def Pricepage(request):
    return render(request,'Faster/price.html',{})

def Contactpage(request):
    return render(request,'Faster/contact.html',{})

def Blogpage(request):
    return render(request,'Faster/blog.html',{})

def singlepage(request):
    return render(request,'Faster/single.html',{})