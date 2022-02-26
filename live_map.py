import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import pandas as pd
import plotly.express as px
import folium
from IPython.display import display
import webbrowser


cleansed_meteorites = pd.read_csv("./data/cleansed-data.csv", delimiter=",")
for col in cleansed_meteorites:
    print(col)

# plt.savefig("./images/testplot.png", format="png")
print("Input a year")
input1 = input()

input2 = int(input1)

mask = cleansed_meteorites['year'] == input2
include = cleansed_meteorites[mask]



map = folium.Map(location=[0, 0], zoom_start=2, control_scale=True)

for index, row in include.iterrows():
    folium.Marker([row["reclat"], row["reclong"]], popup = "Name: " + row["name"] + " Mass: " + str(row["mass"]) + " Fall: " + str(row["fall"]) + " Lat: " + str(row["reclat"]) + " Long: " + str(row["reclong"]) ).add_to(map)




map.save("map.html")
webbrowser.open("map.html")
