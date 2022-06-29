import folium
import pandas


cities=pandas.read_csv(r"D:\10 python apps\App1\volcano_db.csv",encoding='latin-1')
lat=list(cities['Latitude'])
lon=list(cities['Longitude'])
popl=list(cities['Elev'])


def populate_color(population):
    if population < 450000:
        return 'red'
    elif population < 180000:
        return 'blue'
    elif population < 80000:
        return 'gray'
    else:
        return 'green'


map=folium.Map(location=[19.8115,84.7916],zoom_start=6,tiles = "Stamen Terrain")

fg1=folium.FeatureGroup(name='Volcanoes ')

for x,y,z in zip(popl,lat,lon):
    fg1.add_child(folium.CircleMarker(location=[y,z],radius=6,popup=str(x) + ' m',
                                        fill_color=populate_color(x),color='black',fill_opacity=0.7))

fg2=folium.FeatureGroup(name='World Population')
fg2.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                            style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<10000000
                                                        else 'orange' if 10000000<=x['properties']['POP2005']<20000000 else 'red'}))



map.add_child(fg1)
map.add_child(fg2)
map.add_child(folium.LayerControl())
map.save('world_map.html')

