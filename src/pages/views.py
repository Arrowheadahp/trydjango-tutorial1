from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return HttpResponse("<h1>Contacts</h1>")

def about_view(request, *args, **kwargs):
    my_context = {
        'text' :    'my context text', 
        'num' :     420, 
        'list' :    [12, 23, 34],
        'my_html':     '<h1>my_html</h1>',
    }
    return render(request, "about.html", my_context)