import streamlit as st

st.header("||   Meet Our Research Lab Project Team ||")
subheader= ( """
Okeke_Onah GNSS Laboratory (OGL)is an online GPS data processing facility that's free to use. 
It uses localized CORS Network that covers some state in Nigeria. OGL is capable of working with data collected from any 
location within the network and provides differential corrections to any user within the network.
To utilize OGL, simply submit dual-frequency geodetic quality GPS RINEX data that's been observed in a 'static' mode to 
the GPS data processing system.
Once the data has been processed, an OGL report will be sent to you via email""")
st.info(subheader)

col1, col2 = st.columns(2)


with col1:
    st.image("images/FIO.jpg", caption = "Professor Francis I. Okeke\n Supervisor")
    about = """||[Research Gate](https://www.researchgate.net/profile/Francis-Okeke-4)||...............||[UNN - Staff Details](https://staffprofile.unn.edu.ng/profile/1854)|| """
    about


with col2:
    st.image("images/Onah.jpeg", caption = "Surveyor Emmanuel U. Onah\n PhD Student", width=290)
    about = """||[Research Gate](https://www.researchgate.net/profile/Emmanuel-Udochukwu-Onah)||...............||[UNN - Staff Details](https://linkedin.com/in/kingsley-chika-chukwu-235791154/)|| """
    about

