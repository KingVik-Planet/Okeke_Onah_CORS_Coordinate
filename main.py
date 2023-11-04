import streamlit as st
import pandas as pd

col1, col2, = st.columns(2)

with col1:
    st.image("images/photo.jpg")
    #st.image("images/1.png", width = 300)

with col2:
    st.title("Kingsley Chika CHUKWU")
    content = """ 
    Hi, My Name is Kingsley Chika CHUKWU,
    I hold a Diploma and a Bachelor's Degree from Akanu Ibiam Federal Polytechnic, Unwana and 
    [University of Nigeria](https://unn.edu.ng) respectively in the Geoinformatics and Surveying Department
    
I am a Remote Sensing Specialist and Geospatial Scientist, enthusiastic about Artificial Intelligence. I am currently 
working towards becoming a Data Scientist, aiming to integrate Artificial Intelligence and Machine Learning to create 
Geospatial Artificial Intelligence.
"""

    st.info(content)

content2 = """ 
This is my Website which showcase my project built in python.
\nFor any query,  Please Contact me.
"""
st.write(content2)

col3, col4 = st.columns(2)

df = pd.read_csv("data.csv", sep = ";")

with col3:
    for index, row in df[:10].iterrows():
        st.subheader(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"Source Code: {row['url']}")


with col4:
    for index, row in df[10:].iterrows():
        st.subheader(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
