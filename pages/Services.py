import streamlit as st

# st.header("Services")

col1, col2 = st.columns(2)


with col1:
    st.image("images/RS.png", caption="Remote Sensing and Geospatial Science")
    st.title("Remote Sensing and Geospatial Sciences")

with col1:
    st.subheader("1. Flood Inundation, Soil Degradation and impact at Lokoja, Kogi Enviro Nigeria Using Sentinel 1 SAR"
                 " Data on Google Earth Cloud Computing")
    st.image("images/Kogi.png", caption="Google Earth Engine Cloud Computing ")
    App = "[Google Earth Engine Cloud Computing App](https://chukwukingsley56.users.earthengine.app/view/kogiflood2022)"
    App
    st.subheader("Abstract")
    Text1 = " Flood has been "
    Text1


with col2:
    st.image("images/AIML.png", caption="AI/ML")
    st.title("Data Science: Artificial Intelligence  and Machine Learning")
