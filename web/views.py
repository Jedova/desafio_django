from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "web/home.html")

def about(request):
    return render(request, "web/about.html")

def contact(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre", "").strip()
        email = request.POST.get("email", "").strip()
        mensaje = request.POST.get("mensaje", "").strip()
    
        return render(request, "web/contact.html", {"Completo": True, "nombre": nombre})
    return render(request, "web/contact.html")
