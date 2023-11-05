import streamlit as st
from contact_email import contact_email

st.header("Contact me")

with st.form(key = "email_forms"):
    user_name = st.text_input("What is Your Name: ")
    user_email = st.text_input("Enter your Email Address: ")
    message = st.text_area("Your Message: ")
    message + "\n" + user_email
    button = st.form_submit_button("Submit")
    if button:
        contact_email(message)
