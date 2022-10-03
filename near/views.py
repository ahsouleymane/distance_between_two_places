from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from geopy.geocoders import Nominatim
from geopy.distance import geodesic # this fonction calculate distance
import folium
from .utils import *

# Create your views here.

def home(request):

    m = folium.Map(width=1600, height=600, location=[13.521470583129599, 2.1192207657072264], zoom_start=14)

    m = m._repr_html_()

    context = {'map': m}
    return render(request, 'near/index.html', context)

def coordonnees(request):

    coordonnees = Coordonnees.objects.all()
    form = coordonneesForm()

    if request.method == "POST":
        form = coordonneesForm(request.POST)

        if form.is_valid():            
            form.save()
            redirect('/coordonnees/')

    with open('near/data.txt', 'w') as f:
        f_data = f.write(str(coordonneesForm))
        f.close

    with open('near/data.txt', 'r') as f:
        f_contents = f.read()
        print(f_contents) 
        f.close

    context = {'form': form, 'coordonnees': coordonnees, 'f_contents': f_contents}
    return render(request, 'near/coordonnees.html', context)
