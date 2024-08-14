import folium

# Create a map centered in the United States
m = folium.Map(location=[37.0902, -95.7129], zoom_start=3)

# List of places with their approximate coordinates
places = [
    {"name": "Illinois", "location": [40.6331, -89.3985], "status": "lived"},
    {"name": "New York", "location": [40.7128, -74.0060], "status": "lived"},
    {"name": "Florida", "location": [27.9944024, -81.7602544], "status": "lived"},
    {"name": "Indiana", "location": [40.2672, -86.1349], "status": "lived"},
    {"name": "Ohio", "location": [40.4173, -82.9071], "status": "lived"},
    {"name": "Kentucky", "location": [37.8393, -84.2700], "status": "lived"},
    {"name": "Connecticut", "location": [41.6032, -73.0877], "status": "lived"},
    {"name": "South Carolina", "location": [33.8361, -81.1637], "status": "lived"},
    {"name": "Massachusetts", "location": [42.4072, -71.3824], "status": "visited"},
    {"name": "Vermont", "location": [44.5588, -72.5778], "status": "visited"},
    {"name": "New Hampshire", "location": [43.1939, -71.5724], "status": "visited"},
    {"name": "Pennsylvania", "location": [41.2033, -77.1945], "status": "visited"},
    {"name": "Maryland", "location": [39.0458, -76.6413], "status": "visited"},
    {"name": "West Virginia", "location": [38.5976, -80.4549], "status": "visited"},
    {"name": "Virginia", "location": [37.4316, -78.6569], "status": "visited"},
    {"name": "North Carolina", "location": [35.7596, -79.0193], "status": "visited"},
    {"name": "Georgia", "location": [32.1656, -82.9001], "status": "visited"},
    {"name": "Tennessee", "location": [35.5175, -86.5804], "status": "visited"},
    {"name": "Alabama", "location": [32.3182, -86.9023], "status": "visited"},
    {"name": "Mississippi", "location": [32.3547, -89.3985], "status": "visited"},
    {"name": "Louisiana", "location": [30.9843, -91.9623], "status": "visited"},
    {"name": "Louisiana", "location": [30.9843, -91.9623], "status": "visited"},
    {"name": "Arkansas", "location": [34.7465, -92.2896], "status": "visited"},
    {"name": "Missouri", "location": [38.5767, -92.1735], "status": "visited"},
    {"name": "Kansas", "location": [39.0119, -98.4842], "status": "visited"},
    {"name": "Colorado", "location": [39.5501, -105.7821], "status": "visited"},
    {"name": "Nevada", "location": [38.8026, -116.4194], "status": "visited"},
    {"name": "California", "location": [36.7783, -119.4179], "status": "visited"},
    {"name": "Wyoming", "location": [43.07597, -107.2903], "status": "visited"},
    {"name": "Minnesota", "location": [46.7296, -94.6859], "status": "visited"},
    {"name": "Cancun, Mexico", "location": [21.1619, -86.8515], "status": "visited"},
    {"name": "Jamaica", "location": [18.1096, -77.2975], "status": "visited"},
    {"name": "Niagara Falls, Canada", "location": [43.0896, -79.0849], "status": "visited"},
    {"name": "Cozumel, Mexico", "location": [20.4229839, -86.9223432], "status": "visited"},
    {"name": "Grand Cayman", "location": [19.3133, -81.2546], "status": "visited"},
    {"name": "Dominican Republic", "location": [18.7357, -70.1627], "status": "visited"},
    {"name": "New Mexico", "location": [34.5199, -105.8701], "status": "visited"},
]

# Add markers for each place
for place in places:
    color = "blue" if place["status"] == "lived" else "green"
    folium.Marker(
        location=place["location"],
        popup=f'{place["name"]} ({place["status"]})',
        icon=folium.Icon(color=color, icon="info-sign"),
    ).add_to(m)

# Save the map as an HTML file
m.save("travel.html")