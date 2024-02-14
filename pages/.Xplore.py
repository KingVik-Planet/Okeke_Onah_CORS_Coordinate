import streamlit as st
from scipy.interpolate import griddata
import numpy as np


def main():
    st.title("Interpolation App")

    # Known station data
    station_data = {
        "ABUZ": {"lat": 6.315055601, "lon": 8.122842036, "height": 49.771},
        "ABIA": {"lat": 5.524274111, "lon": 7.520314611, "height": 159.203},
        "ASAB": {"lat": 6.19500475, "lon": 6.719156056, "height": 54.877},
        "GEOS": {"lat": 6.330945781, "lon": 5.638304722, "height": 91.143},
        "OSUN": {"lat": 7.752762361, "lon": 4.52582788, "height": 326.628},
        "WARR": {"lat": 5.567309747, "lon": 5.8100107, "height": 16.382}
    }

    # Extracting latitudes, longitudes, and heights
    lats = [station_data[station]["lat"] for station in station_data]
    lons = [station_data[station]["lon"] for station in station_data]
    heights = [station_data[station]["height"] for station in station_data]

    # Get new station data from user input
    new_station_name = st.text_input("Enter new point name:")
    new_station_lat = st.number_input("Enter new point latitude:")
    new_station_lon = st.number_input("Enter new point longitude:")
    new_station_height = st.number_input("Enter new point height:")

    # Interpolate the new station data for latitude and longitude separately
    methods = ['nearest', 'linear', 'cubic']
    for method in methods:
        interpolated_lat = griddata((lats, lons), lats, (new_station_lat, new_station_lon), method=method)
        interpolated_lon = griddata((lats, lons), lons, (new_station_lat, new_station_lon), method=method)
        interpolated_height = griddata((lats, lons), heights, (new_station_lat, new_station_lon), method=method)

        st.write(f"Result for method: {method.capitalize()}:")
        st.write(f"Interpolated Latitude: {interpolated_lat:.6f}")
        st.write(f"Interpolated Longitude: {interpolated_lon:.6f}")
        st.write(f"Interpolated Height: {interpolated_height:.2f}")
        st.write("Adjustment:")
        for station, data in station_data.items():
            lat_diff = interpolated_lat - data["lat"]
            lon_diff = interpolated_lon - data["lon"]
            height_diff = interpolated_height - data["height"]
            st.write(
                f"{station} to {new_station_name} - Lat: {lat_diff:.2f}, Lon: {lon_diff:.2f}, Height: {height_diff:.2f}")
        st.write()


if __name__ == "__main__":
    main()
