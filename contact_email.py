import smtplib, ssl
import streamlit as st

st.title("EmmaFIOkeke CORS_Coordinate")
content = """Hi, My Name is Kingsley Chika CHUKWU, I hold a Diploma and a Bachelor's Degree from [Akanu Ibiam 
    Federal Polytechnic, Unwana](https://polyunwana.edu.ng/) and [University of Nigeria](https://unn.edu.ng) 
    respectively in the Geoinformatics and Surveying Department, MSc in Environmental Information System (EIS) from UNILAK, Rwanda

I am a Remote Sensing Specialist and Geospatial Scientist, enthusiastic about Artificial Intelligence and Machine learning. I am currently 
working towards becoming a Data Scientist, aiming to integrate Artificial Intelligence and Machine Learning to create 
Geospatial Artificial Intelligence..
"""
st.info(content)

def contact_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "chukwukingsley56@gmail.com" #"Your Email Address or Username Like: chukwukingsley56@gmail.com"
    password = "riwy cigx jwnx zdrb" #Passowrd
    reciever = "chukwukingsley56@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciever, message)
