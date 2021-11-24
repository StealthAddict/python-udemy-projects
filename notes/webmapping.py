# HOW TO MAKE A WEBMAP
import folium
import pandas

map = folium.Map(location=[90,60], tiles= "Stamen Terrain")



# ADDING POINTS

# Organize marker children into FeatureGroup
featgrp = folium.FeatureGroup(name= "My Map")

featgrp.add_child(folium.Marker(location=[1,1], popup="handmarker1", icon= folium.Icon(color='red')))
featgrp.add_child(folium.Marker(location=[2,2], popup="handmarker2", icon= folium.Icon(color='red')))

# Adds all above markers
map.add_child(featgrp)

# More efficient through for loop
for coords in [[10,50],[50,122]]:
    featgrp.add_child(folium.Marker(location=coords, popup="loopmarker", icon= folium.Icon(color='blue')))

map.add_child(featgrp)

# Add markers through a text file
#   Requries pandas

data = pandas.read_csv("C:/Users/Of The Crow/Documents/VSCODE/PYTHON/Udemycourse/volcanotxt.txt")
latitude = list(data["LAT"])
longitude = list(data["LON"])
elevation = list(data["ELEV"])

#   Extra: Add HTML!
html = """<h4>Volcano information:</h4>
Height: %s m
"""

for lat, lon, elev in zip(latitude, longitude, elevation):
    iframe = folium.IFrame(html=html % str(elev), width= 200, height= 100)
    featgrp.add_child(folium.Marker(location=[lat, lon], popup=folium.Popup(iframe), icon= folium.Icon(color='cadetblue')))




# SAVE MAP
map.save("testmap.html")