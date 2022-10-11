from django.shortcuts import render, redirect, get_object_or_404
from geopy.geocoders import Nominatim
from geopy.distance import geodesic # this fonction calculate distance
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

from .forms import *
from .models import *
from .utils import *

import folium
import requests
import json, urllib
import fileinput

# Create your views here.

def home(request):

    #### Distances calculation

    # Initial values
    distance = None
    destination = None

    # Location coordinates using json
    r = requests.get('https://get.geojs.io/')
    ip_request = requests.get('https://get.geojs.io/v1/ip.json')
    ip_add = ip_request.json()['ip']
    #print(ip_add)

    url = 'https://get.geojs.io/v1/ip/geo/'+ip_add+'.json'
    geo_request = requests.get(url)
    geo_data = geo_request.json()
    #print(geo_data)

    # Location coordinates
    x_lat = float(geo_data['latitude'])
    x_lon = float(geo_data['longitude'])
    #print(x_lat, x_lon)

    pointA = (x_lat, x_lon)

    # Destination coordinates
    #d_lat = destination.latitude
    #d_lon = destination.longitude

    #pointB = (d_lat, d_lon)

    #### Get coordinates in file

    listOf = []
    listOfLocation = []
    listOfLat = []
    listOfLon = []

    with open('coordonnees.txt', 'r') as file:
        count = 1
        locationIndex = count + 1
        latIndex = count + 2
        lonIndex = count + 3
        
        for line in file.readlines():
            listOf.append(line)

            if count == locationIndex:
                listOfLocation.append(line)
                locationIndex = count + 4

            if count == latIndex:
                listOfLat.append(line)
                latIndex = count + 4

            if count == lonIndex:
                listOfLon.append(line)
                lonIndex = count + 4

            count += 1

    print("\n")
    print("List of:\n")
    print(listOf)
    print("\n")
    print("List of location:\n")
    print(listOfLocation)
    print("\n")
    print("List of latitude:\n")
    print(listOfLat)
    print("\n")
    print("List of longitude:\n")
    print(listOfLon)
    print("\n")
    print("Number of element:\n")
    print(count)

    print("\n")
       

    #### Distance calculation

    #distance = round(geodesic(pointA, pointB).km, 2)

    m = folium.Map(width=1600, height=600, location=[13.521470583129599, 2.1192207657072264], zoom_start=14)

    m = m._repr_html_()

    context = {'map': m}
    return render(request, 'near/index.html', context)

# Save coordinates in database and file

def save_coordinates_in_db_and_file(request):

    form = coordonneesForm()

    if request.method == "POST":
        form = coordonneesForm(request.POST)

        if form.is_valid():            
            form.save()
            redirect('/save_coordinates_in_db/')

    #### Get all object of database and insert in a file

    coordonnees = Coordonnees.objects.all()

    with open('coordonnees.txt', 'w') as file:

        for coordonnee in coordonnees:

            # Write in text file
            file.writelines(f'{coordonnee.id}\n{coordonnee.emplacement}\n{coordonnee.latitude}\n{coordonnee.longitude}\n')

        file.close()

    context = {'form': form, 'coordonnees': coordonnees}
    return render(request, 'near/coordonnees.html', context)




# Generate coordinates in text file

""" def generate_coordinates_in_file(request):

    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=coordonnees.txt'

    coordonnees = Coordonnees.objects.all()

    lines = []

    for coordonnee in coordonnees:
        lines.append(f'{coordonnee.id}\n{coordonnee.emplacement}\n{coordonnee.latitude}\n{coordonnee.longitude}\n\n\n')

    # Write in text file

    response.writelines(lines)
    
    return response

 """