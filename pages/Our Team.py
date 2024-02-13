import streamlit as st

st.header("||   Meet Our Research Project Team ||")

col1, col2 = st.columns(2)


with col1:
    st.image("images/FIO.jpg", caption = "Professor Francis I. Okeke\n Supervisor")
    about = """||[Research Gate](https://www.researchgate.net/profile/Francis-Okeke-4)||...............||[UNN - Staff Details](https://staffprofile.unn.edu.ng/profile/1854)|| """
    about


with col2:
    st.image("images/Onah.jpeg", caption = "Surveyor Emmanuel U. Onah\n PhD Student", width=290)
    about = """||[Research Gate](https://www.researchgate.net/profile/Emmanuel-Udochukwu-Onah)||...............||[UNN - Staff Details](https://linkedin.com/in/kingsley-chika-chukwu-235791154/)|| """
    about

