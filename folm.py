import folium
import webbrowser
m = folium.Map(location =[28.644800, 77.216721])
m.save ("map.html")
webbrowser.open("map.html")