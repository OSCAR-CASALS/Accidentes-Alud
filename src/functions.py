import folium
from folium.plugins import MarkerCluster

def create_map(DataFrame, colorVariable):
    #Define coordinates of where we want to center our map
    boulder_coords = [40.416775, -3.703790]

    #Create the map
    my_map = folium.Map(location = boulder_coords, zoom_start = 5)

    # Add markers

    for i in range(0,len(DataFrame)):
        Death = int(DataFrame.iloc[i][colorVariable])

        Color = "gray"

        if Death == 0:
            Color = "darkgreen"
        elif Death == -1:
            Color = "gray"
        elif Death < 3:
            Color = "orange"
        else:
            Color = "darkred"

        folium.Marker(
            location=[DataFrame.iloc[i]['lat'], DataFrame.iloc[i]['long']],
            popup=DataFrame.iloc[i]['Lloc'],
            icon = folium.Icon(icon="globe", color = Color),
        ).add_to(my_map)

    #Display the map
    return my_map