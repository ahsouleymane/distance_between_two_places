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

    geolocator = Nominatim(user_agent='near')
    country, city, lat, lon = get_geo(ip_add)
    location = geolocator.geocode(city)

    
    number_of_location = Coordonnees.objects.all().count()
    #print('Number of location: ', number_of_location)

    locations = []

    parcourt = 0
    while parcourt < number_of_location:

        locations = Coordonnees.objects.values_list('emplacement', flat=True)
        parcourt += 1

    #print(locations)


    latitudes = []
    longitudes = []

    parcourt = 0
    while parcourt < number_of_location:

        latitudes = Coordonnees.objects.values_list('latitude', flat=True)
        longitudes = Coordonnees.objects.values_list('longitude', flat=True)

        parcourt += 1

    #print(latitudes)
    #print(longitudes)

    distances = []

    parcourt = 0
    while parcourt < number_of_location and parcourt < len(latitudes) and parcourt < len(longitudes):
        
        d_lat = latitudes[parcourt]
        d_lon = longitudes[parcourt]

        pointB = (d_lat, d_lon)

        # calculate distance
        distance = round(geodesic(pointA, pointB).km, 2)

        distances.append(locations[parcourt] + ': ' + str(distance) + ' Km')

        parcourt += 1



    print("\n")
    print("List of distances for all location and distances:\n")

    m = folium.Map(width=1600, height=600, location=get_center_coordinates(x_lat, x_lon), zoom_start=14)

    # Location marker
    folium.Marker([x_lat, x_lon], tooltip='click here for more', popup=city['city'], 
                    icon=folium.Icon(color='purple')).add_to(m)

    m = m._repr_html_()

    context = {'map': m, 'distances': distances}
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