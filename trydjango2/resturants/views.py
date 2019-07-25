from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View


def home_view(request): #first parameter that is needed to run the application, is set default by the django application,
    # (containing info about user such as username, ip address  etc) and browser
    context ={      #data that will be fetched to user
        "resturants" : "109deg",
        "Location": "Siphal",
        "items":['asdasd', "mahsgh"]
    }
    return render(request,"home.html",context) #render : since the django application doesn't understand the jinja templates so it converts them to proper django render also helps to connect between those two.





class HomeView(View):

    def get(self, request):
        return render(request, "hotel.html",{})

class WelcomeTemplateView(TemplateView):
    template_name = "hotel.html"

    def get_context_data(self, **kwargs):
        context = {
            "resturant_name":"Bajeko sekuwa",
            "Location":"Baneswor"
        }
        return context


class AboutTemplateView(TemplateView):
    template_name = "hotel.html"

# Create your views here.
