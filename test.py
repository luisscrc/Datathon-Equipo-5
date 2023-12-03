
import numpy as np

import matplotlib.pyplot as plt
import sklearn
import cudf.pandas
# pandas API is now GPU accelerated

import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

geolocator = Nominatim(user_agent="my_geocoder")
geolocation_cache = {}

# Function to obtain geolocation coordinates from a postal code
def obtener_coordenadas_osm(codigo_postal):
    if codigo_postal in geolocation_cache:
        return geolocation_cache[codigo_postal]

    location = geolocator.geocode({"postalcode": codigo_postal})
    if location:
        coords = (location.latitude, location.longitude)
        geolocation_cache[codigo_postal] = coords
        return coords
    else:
        return None

# Function to calculate the distance between two postal codes
def calcular_distancia_osm(cp_empleado, cp_bosch):
    coords_empleado = obtener_coordenadas_osm(cp_empleado)
    coords_bosch = obtener_coordenadas_osm(cp_bosch)

    if coords_empleado and coords_bosch:
        distancia = geodesic(coords_empleado, coords_bosch).kilometers
        return distancia
    else:
        return None

# Insert a column called "Codigo Postal Bosch" with the value 32557
df['CODIGO POSTAL BOSCH'] = 32557

# Calculate the distance between the employee and Bosch
if 'C.P.' in df.columns and 'CODIGO POSTAL BOSCH' in df.columns:
    df['distancia'] = df.apply(lambda x: calcular_distancia_osm(x['C.P.'], x['CODIGO POSTAL BOSCH']), axis=1)
    df.head()