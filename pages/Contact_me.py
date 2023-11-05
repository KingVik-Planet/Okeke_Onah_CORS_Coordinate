import streamlit as st

st.header("Contact me")

with st.form(key = "email_forms"):
    user_email = st.text_input("Enter your Email Address: ")
    message = st.text_area("Your Message: ")
    button = st.form_submit_button("Submit")
    if button:
        print(button)
        print("""Your Message Has Been Submitted Successfully \nThank you, we will get back to you soonest""")
