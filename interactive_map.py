import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import pandas as pd
import plotly.express as px
# import folium
from folium.plugins import HeatMap
from IPython.display import display
import webbrowser
import os
from folium import plugins, Map, Marker
from folium.plugins import HeatMap



# Clean Up Data Section

meteorites = pd.read_csv("./data/meteorite-landings.csv", delimiter=",")
# Rename columns
meteorites = meteorites.rename(columns={'name': 'Name', 'id': 'ID', 'nametype': 'Type', 'recclass': 'Class', 'mass': 'Mass', 'fall': 'Fell', 'year': 'Year', 'reclat': 'Latitude', 'reclong': 'Longitude'})
# Get rid of faulty datapoints
filtered_coords = (meteorites["Longitude"] >= -180) & (meteorites["Longitude"] <= 180) & ((meteorites["Longitude"] != 0) | (meteorites["Latitude"] != 0))
filtered_years = (meteorites["Year"] >= 860) & (meteorites["Year"] <= 2016)
filtered_mass = ((meteorites["Mass"] >= 100))
filtered_type = ((meteorites["Type"] == "Valid"))
filtered_meteorites = meteorites[filtered_coords & filtered_years & filtered_type]
filtered_meteorites.drop(["GeoLocation", "Type"], axis=1, inplace=True)
filtered_meteorites.to_csv("./data/cleansed-data.csv")
filtered_meteorites = filtered_meteorites.sort_values(by="Year", ascending=True)


cleansed_meteorites = pd.read_csv("./data/cleansed-data.csv", delimiter=",")
start_year = int(input("Input start year: "))
end_year = int(input("Input end year: "))



mask = (cleansed_meteorites["Year"] >= start_year) & (cleansed_meteorites["Year"] <= end_year)
include = cleansed_meteorites[mask]
min_mass = int(input(""))

mask = cleansed_meteorites[mask]


map = Map(location=[0, 0], zoom_start=2, control_scale=True)

for index, row in include.iterrows():
    Marker([row["Latitude"], row["Longitude"]], popup = "Name: " + row["Name"] + " Mass: " + str(row["Mass"]) + " Fall: " + str(row["Fell"]) + " Lat: " + str(row["Latitude"]) + " Long: " + str(row["Longitude"]) ).add_to(map)

mask = mask[['Latitude', 'Longitude']]
# mask = mask.dropna(axis=0, subset=['Latitude','Longitude'])
map_data = [[row['Latitude'],row['Longitude']] for index, row in mask.iterrows()]
HeatMap(map_data).add_to(map)


map.save("map.html")
webbrowser.open("map.html")
webbrowser.open('file://' + os.path.realpath("map.html")) # open file in default browser