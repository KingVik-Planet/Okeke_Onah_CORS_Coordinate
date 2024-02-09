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

