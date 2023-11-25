import streamlit as st

# st.header("Services")

col1, col2 = st.columns(2)


with col1:
    st.image("images/RS.png", caption="Remote Sensing and Geospatial Science")
    st.title("Remote Sensing and Geospatial Sciences")



with col2:
    st.image("images/AIML.png", caption="AI/ML")
    st.title("Data Science: Artificial Intelligence  and Machine Learning")
