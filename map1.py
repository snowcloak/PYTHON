import folium
import pandas as pd

#read data/csv
data = pd.read_csv("Files/Volcanoes.txt")

#create lists from dataframe
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

#stylizing with HTML (know HTML)
html = """
<b><br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br></b>
Height: %s m
"""
#adding functions
def colorProducer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

#set up the map, my choice was the center of the US
map = folium.Map(location=[39.50, -98.35], zoom_start=6, tiles="Stamen Terrain")

#create a feature group
#feature group for volcanoes
fgv = folium.FeatureGroup(name="Volcanoes")

#when doing multiple lists, you must use zip()
#read more on zip()
for lt, ln, el, name in zip(lat, lon, elev, name):
    #stylize with HTML
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    #adding to a feature group
    fgv.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe, parse_html=True), icon=folium.Icon(icon="cloud", color=colorProducer(el))))
    
    #alternative with CircleMarker
    #fg.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=folium.Popup(iframe, parse_html=True), color='grey', fill_opacity=0.7, fill_color=colorProducer(el)))

#freature group for population
fgp = folium.FeatureGroup(name="My Map")

#adding a polygon layer
#lambda function
fgp.add_child(folium.GeoJson(data=open("Files/world.json", 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 < x['properties']['POP2005'] < 20000000
else 'red'}))

#adding feature group to the map
map.add_child(fgv)
map.add_child(fgp)

#add layer control AFTER a feature group
map.add_child(folium.LayerControl())

map.save("map1.html")