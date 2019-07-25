from django.shortcuts import render

def hotel_view(request):  #request are the initial statement to be passed in the first run
    context = {
        "Name" : "Moonlight",
        "location" : ["chhetrapati", "Nakkhipot"]

    }
    return render(request,"hotel.html", context)

def contact(request):
    return render(request, "contact.py", context={})
# Create your views here.
