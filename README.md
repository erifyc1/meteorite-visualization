# Meteorite Visualization
# HackIllinois 2022

## Introduction:

Video: https://youtu.be/p171Nv6yP4I </br>

Our project is a visualization of meteorite findings using multiple mediums and representations. With different perspectives on the visualization of this data, we hope to be able to draw new conclusions based on the patterns we find.

As we considered which topics we wanted to pursue for the hackathon, we took heavy inspiration from the physics and engineering background of our members. Scientists have often relied on meteorites to study the early solar system and how impacts have altered Earth’s formation. By using various libraries to visualize an extensive dataset of these landings, we can better identify common patterns relating the distribution of meteorite landings and their respective locations, masses, and types across the Earth. These visualizations could aid astronomers in their study of the solar system.

While creating our project, we learned a lot about different plotting tools in python. At first, we defaulted to using matplotlib due to it being the easiest and one of the most well-known data visualization libraries for python, but we soon discovered that it didn’t best suit our needs. We expanded into other packages, such as plotly and folium, that we previously had little to no experience in. These packages allowed us to create extremely interesting visualizations, such as a heatmap and a timeline animation. We also used standard packages such as pandas and numpy to manipulate data efficiently.

Our struggles during this project mostly consisted of us trying to learn new packages by constantly reading documentation and attempting to properly manage version control with Git. Specifically, since we did not know about packages such as plotly and folium before, none of us knew how to apply them to a large dataset. Also, since we were not all equally proficient with Git, it was difficult to work out merge conflicts initially before we eventually created multiple branches to ensure that we could work in parallel.

## File Descriptions
1. [interactive_map.py](interactive_map.py): Interactive Heat Map with overlaid meteorite info. User can input time period to analyze and minimum mass of meteorite for plot points on map
2. [animation.ipynb](animation.ipynb): Animation of meteorites found over time, color and size of points scaled by mass
3. [misc_visualization.ipynb](misc_visualization.ipynb): Several basic visualizations
4. [metrics.ipynb](metrics.ipynb): Visualizations based on class of meteorite
5. [animation.html](images/animation.html): animation file output after running [animation.ipynb](animation.ipynb)
6. [map.html](map.html): animation file output after running [interactive_map.py](interactive_map.py)

## Authors
1. Arhan Goyal
2. Ben Guan
3. Evan Coats
4. Jacob Stolker
5. Sary Bseiso

