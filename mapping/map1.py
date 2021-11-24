import folium
import pandas

# Prepping external data
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elevation = list(data["ELEV"])

# Changing marker color
def color_producer(el):
    if el < 1000:
        return 'green'
    elif 1000 <= el < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58, -99.09], zoom_start = 6, tiles = "Stamen Terrain")

# Organize children in FeatureGroups
ftg_mark = folium.FeatureGroup(name= "Volcanoes")
ftg_poly = folium.FeatureGroup(name= "Population")

# Create markers (circles)
for latit, longi, elev in zip(lat, lon, elevation):
    ftg_mark.add_child(folium.CircleMarker(location=[latit, longi], popup=folium.Popup(str(elev) + "m", parse_html=True),
     radius= 5, fill_color= color_producer(elev), color= color_producer(elev)))

# Create polygons from json file & show population from file
ftg_poly.add_child(folium.GeoJson(data= open('world.json', 'r', encoding='utf-8-sig').read(),
style_function= lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 10000000
 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red', 'color':'black'}))



# Adds all above markers
map.add_child(ftg_mark)
map.add_child(ftg_poly)

# Control the layers
map.add_child(folium.LayerControl())



# Save map
map.save("Map1.html")