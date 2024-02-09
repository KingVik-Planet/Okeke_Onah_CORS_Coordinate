import streamlit as st
import pandas as pd

col1, col2 = st.columns(2)

with col1:
    st.image("images/UNN.png", caption = "University of Nigeria Enugu Campuss")
    links = """|| [Twitter](https://twitter.com/KingVik_Planet) || 
    [Linkedin](https://linkedin.com/in/kingsley-chika-chukwu-235791154/) || [FaceBook](unn.edu.ng) ||
    [WikiMedia](wikiik) || [OpenStreetMap](fagfajjfk)|| [Instagram](fjdfbuibdif) ||
    """
    st.info(links)
    #st.image("images/1.png", width = 300)


with col2:
    st.title("EmmaFIOkeke CORS_Coordinate")
    content = """Hi, My Name is Kingsley Chika CHUKWU, I hold a Diploma and a Bachelor's Degree from [Akanu Ibiam 
    Federal Polytechnic, Unwana](https://polyunwana.edu.ng/) and [University of Nigeria](https://unn.edu.ng) 
    respectively in the Geoinformatics and Surveying Department, MSc in Environmental Information System (EIS) from UNILAK, Rwanda
    
I am a Remote Sensing Specialist and Geospatial Scientist, enthusiastic about Artificial Intelligence and Machine learning. I am currently 
working towards becoming a Data Scientist, aiming to integrate Artificial Intelligence and Machine Learning to create 
Geospatial Artificial Intelligence..
"""

    st.info(content)

with col1:
    import streamlit as st
    import folium
    import numpy as np
    from streamlit_folium import folium_static


    def main():
        # Station data
        station_data = {
            "ABUZ": {"lat": 11.15173972, "lon": 7.64868722, "height": 705.0661},
            "BKFP": {"lat": 12.46857667, "lon": 4.22924194, "height": 250.0116},
            "CGGT": {"lat": 10.12309472, "lon": 9.11831167, "height": 916.4457},
            "CLBR": {"lat": 4.95030139, "lon": 8.35156917, "height": 57.21},
            "FUTY": {"lat": 9.3497425, "lon": 12.49779778, "height": 247.4062},
            "RUST": {"lat": 4.80183583, "lon": 6.97852139, "height": 45.589},
            "ULAG": {"lat": 6.51732639, "lon": 3.39762333, "height": 44.5752},
            "UNEC": {"lat": 6.42480583, "lon": 7.50499111, "height": 254.4058},
        }

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

        # Display the map using Streamlit's `st` function
        folium_static(m)


    if __name__ == "__main__":
        main()

