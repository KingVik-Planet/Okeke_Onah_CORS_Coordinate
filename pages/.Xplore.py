import streamlit as st
import folium
import numpy as np
from scipy.interpolate import griddata
from pyproj import Proj, transform
from streamlit_folium import folium_static
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io
from geopy.distance import geodesic

# Function to calculate distance between two coordinates using Haversine formula
def calculate_distance(coord1, coord2):
    return geodesic(coord1, coord2).kilometers

# Function to convert LLH to UTM
def llh_to_utm(lat, lon, height):
    utm_zone = int((lon + 180) / 6) + 1  # UTM zone calculation
    p = Proj(proj="utm", zone=utm_zone, ellps="WGS84", preserve_units=False)
    utm_x, utm_y = p(lon, lat)
    return utm_x, utm_y, height

# Function to add UTM coordinates to station data
def add_utm_coordinates(station_data):
    for station, data in station_data.items():
        lat, lon, height = data["lat"], data["lon"], data["height"]
        utm_x, utm_y, utm_z = llh_to_utm(lat, lon, height)
        data["utm_x"] = utm_x
        data["utm_y"] = utm_y
        data["utm_z"] = utm_z

# Known station data
station_data = {
    "ABUZ": {"lat": 6.315055601, "lon": 8.122842036, "height": 49.771},
    "ABIA": {"lat": 5.524274111, "lon": 7.520314611, "height": 159.203},
    "ASAB": {"lat": 6.19500475, "lon": 6.719156056, "height": 54.877},
    "GEOS": {"lat": 6.330945781, "lon": 5.638304722, "height": 91.143},
    "OSUN": {"lat": 7.752762361, "lon": 4.52582788, "height": 326.628},
    "WARR": {"lat": 5.567309747, "lon": 5.8100107, "height": 16.382}
}

# Add UTM coordinates to station data
add_utm_coordinates(station_data)

# Extracting latitudes, longitudes, and heights
lats = [station_data[station]["lat"] for station in station_data]
lons = [station_data[station]["lon"] for station in station_data]
heights = [station_data[station]["height"] for station in station_data]

# Create Streamlit app
st.title("Interpolation and Adjustment Calculator")

# User input for new station
st.subheader("Enter New Station Details")
new_station_name = st.text_input("Name")
new_station_lat = st.number_input("Latitude", format="%.10f")
new_station_lon = st.number_input("Longitude", format="%.10f")
new_station_height = st.number_input("Height", format="%.10f")

# New station data
new_station = {
    "name": new_station_name,
    "lat": new_station_lat,
    "lon": new_station_lon,
    "height": new_station_height
}


# Calculate UTM coordinates for the new station
new_station["utm_x"], new_station["utm_y"], new_station["utm_z"] = llh_to_utm(new_station["lat"], new_station["lon"], new_station["height"])

# Interpolation methods
methods = ['nearest', 'linear', 'cubic']

# Create PDF function
def create_pdf(method, interpolated_lat, interpolated_lon, interpolated_height):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    c.drawString(100, 750, f"Interpolation and Adjustment Report ({method.capitalize()})")
    y = 700

    c.drawString(100, y, f"Interpolation Result for method: {method.capitalize()}")
    y -= 20
    c.drawString(100, y, f"Inputted Latitude: {new_station['lat']:.10f}, Interpolated Latitude: {interpolated_lat:.10f}, Difference: {new_station['lat'] - interpolated_lat:.10f}")
    y -= 20
    c.drawString(100, y, f"Inputted Longitude: {new_station['lon']:.10f}, Interpolated Longitude: {interpolated_lon:.10f}, Difference: {new_station['lon'] - interpolated_lon:.10f}")
    y -= 20
    c.drawString(100, y, f"Inputted Height: {new_station['height']:.10f}, Interpolated Height: {interpolated_height:.10f}, Difference: {new_station['height'] - interpolated_height:.10f}")

    # Adjustment (Geographic)
    y -= 40
    c.drawString(100, y, "Adjustment (Geographic)")
    y -= 20
    for station, data in station_data.items():
        lat_diff = interpolated_lat - data["lat"]
        lon_diff = interpolated_lon - data["lon"]
        height_diff = interpolated_height - data["height"]
        c.drawString(100, y, f"{station} to {new_station['name']} - Lat: {new_station['lat'] - lat_diff:.10f}, Lon: {new_station['lon'] - lon_diff:.10f}, Height: {new_station['height'] - height_diff:.10f}")
        y -= 20

    # Adjustment (UTM)
    y -= 40
    c.drawString(100, y, "Adjustment (UTM)")
    utm_x_diff = new_station["utm_x"] - station_data[station]["utm_x"]
    utm_y_diff = new_station["utm_y"] - station_data[station]["utm_y"]
    utm_z_diff = new_station["utm_z"] - station_data[station]["utm_z"]
    for station, data in station_data.items():
        c.drawString(100, y, f"{station} to {new_station['name']} - UTM_X: {new_station['utm_x'] + utm_x_diff:.10f}, UTM_Y: {new_station['utm_y'] + utm_y_diff:.10f}, UTM_Z: {new_station['utm_z'] + utm_z_diff:.10f}")
        y -= 20

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer

# Perform interpolation and display results
for method in methods:
    interpolated_lat = griddata((lats, lons), lats, (new_station["lat"], new_station["lon"]), method=method)
    interpolated_lon = griddata((lats, lons), lons, (new_station["lat"], new_station["lon"]), method=method)
    interpolated_height = griddata((lats, lons), heights, (new_station["lat"], new_station["lon"]), method=method)

    st.subheader(f"Interpolation Result for method: {method.capitalize()}")
    st.write(f"Inputted Latitude: {new_station['lat']:.10f}, Interpolated Latitude: {interpolated_lat:.10f}, Difference: {new_station['lat'] - interpolated_lat:.10f}")
    st.write(f"Inputted Longitude: {new_station['lon']:.10f}, Interpolated Longitude: {interpolated_lon:.10f}, Difference: {new_station['lon'] - interpolated_lon:.10f}")
    st.write(f"Inputted Height: {new_station['height']:.10f}, Interpolated Height: {interpolated_height:.10f}, Difference: {new_station['height'] - interpolated_height:.10f}")

    # Calculate and print distances to known stations
    st.subheader("Distances to Known Stations")
    for station, data in station_data.items():
        coord_new_station = (new_station["lat"], new_station["lon"])
        coord_known_station = (data["lat"], data["lon"])
        distance = calculate_distance(coord_new_station, coord_known_station)
        st.write(f"Distance from {new_station['name']} to {station}: {distance:.2f} km")

    # Adjustment (Geographic)
    st.subheader("Adjustment (Geographic)")
    for station, data in station_data.items():
        lat_diff = interpolated_lat - data["lat"]
        lon_diff = interpolated_lon - data["lon"]
        height_diff = interpolated_height - data["height"]
        st.write(f"{station} to {new_station['name']} - Lat: {new_station['lat'] - lat_diff:.10f}, Lon: {new_station['lon'] - lon_diff:.10f}, Height: {new_station['height'] - height_diff:.10f}")

    # Adjustment (UTM)
    st.subheader("Adjustment (UTM)")
    utm_x_diff = new_station["utm_x"] - station_data[station]["utm_x"]
    utm_y_diff = new_station["utm_y"] - station_data[station]["utm_y"]
    utm_z_diff = new_station["utm_z"] - station_data[station]["utm_z"]
    for station, data in station_data.items():
        st.write(f"{station} to {new_station['name']} - UTM_X: {new_station['utm_x'] + utm_x_diff:.10f}, UTM_Y: {new_station['utm_y'] + utm_y_diff:.10f}, UTM_Z: {new_station['utm_z'] + utm_z_diff:.10f}")

    # Generate PDF button
    pdf_buffer = create_pdf(method, interpolated_lat, interpolated_lon, interpolated_height)
    st.download_button(label=f"Download PDF ({method.capitalize()})", data=pdf_buffer, file_name=f"interpolation_report_{method}.pdf", mime="application/pdf")
    st.write("\n")

# Create a Folium map centered around the mean of latitudes and longitudes
m = folium.Map(location=[np.mean(list(map(lambda x: x["lat"], station_data.values()))),
                         np.mean(list(map(lambda x: x["lon"], station_data.values())))],
               zoom_start=6, control_scale=True)

# Add markers for each station
for station, data in station_data.items():
    folium.Marker(
        location=[data["lat"], data["lon"]],
        popup=f"{station} ({data['lat']}, {data['lon']}, {data['height']})",
        icon=folium.Icon(color="blue"),
    ).add_to(m)

# Add marker for the new station
folium.Marker(
    location=[new_station["lat"], new_station["lon"]],
    popup=f"{new_station['name']} ({new_station['lat']}, {new_station['lon']}, {new_station['height']})",
    icon=folium.Icon(color="green"),
).add_to(m)

# Display the map using Streamlit's `st` function
st.markdown("""
    <div style='text-align: center; background-color: lightgreen; border-radius: 5px; padding: 1px;'>
        <h4 style='color: blue;'>Map with Stations (Known Stations [Blue] & New Station [Green])</h4>
    </div>
""", unsafe_allow_html=True)
folium_static(m)



