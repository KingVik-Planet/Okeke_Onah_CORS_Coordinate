import streamlit as st

st.header("Meet Our Team")

col1, col2 = st.columns(2)


with col1:
    st.image("images/photo.jpg", caption = "Professor Francis I. Okeke\n Supervisor")
    about = """||[Twitter](https://twitter.com/KingVik_Planet)||[Linkedin](https://linkedin.com/in/kingsley-chika-chukwu-235791154/)|| """
    about


with col2:
    st.image("images/photo.jpg", caption = "Surveyor Emmanuel U. Onah\n PhD Student")
    about = """||[Twitter](https://twitter.com/KingVik_Planet)||[Linkedin](https://linkedin.com/in/kingsley-chika-chukwu-235791154/)|| """
    about

