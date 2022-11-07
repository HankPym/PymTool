import folium

map_1 = folium.Map(location=[43.040492,-70.7642883],
                   zoom_start=18,
                   tiles='OpenStreetMap')
folium.Marker([45.3288, -121.6625], popup='Mt. Hood Meadows').add_to(map_1)
folium.Marker([45.3311, -121.7113], popup='Timberline Lodge').add_to(map_1)
map_1.save('/Users/lfister/OneDrive/Code/data/output.html')