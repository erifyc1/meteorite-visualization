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
from folium import plugins, Map
from folium.plugins import HeatMap


cleansed_meteorites = pd.read_csv("./data/cleansed-data.csv", delimiter=",")
for col in cleansed_meteorites:
    print(col)

# plt.savefig("./images/testplot.png", format="png")
start_year = int(input("Input start year: "))
end_year = int(input("Input end year: "))


mask = (cleansed_meteorites["Year"] >= start_year) & (cleansed_meteorites["Year"] <= end_year)
# include = cleansed_meteorites[mask]
mask = cleansed_meteorites[mask]


map = Map(location=[0, 0], zoom_start=2, control_scale=True)

# for index, row in include.iterrows():
#     folium.Marker([row["Latitude"], row["Longitude"]], popup = "Name: " + row["Name"] + " Mass: " + str(row["Mass"]) + " Fall: " + str(row["Fell"]) + " Lat: " + str(row["Latitude"]) + " Long: " + str(row["Longitude"]) ).add_to(map)

mask = mask[['Latitude', 'Longitude']]
# mask = mask.dropna(axis=0, subset=['Latitude','Longitude'])
map_data = [[row['Latitude'],row['Longitude']] for index, row in mask.iterrows()]
HeatMap(map_data).add_to(map)


map.save("map.html")
webbrowser.open("map.html")
webbrowser.open('file://' + os.path.realpath("map.html")) # open file in default browser