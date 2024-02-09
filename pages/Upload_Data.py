import streamlit as st
from contact_email import contact_email

st.header("Uploading the Data to be Processed")

with st.form(key="email_forms"):
    user_name = st.text_input("Which Name Should I Address You With?: (Compulsory) ")
    user_email = st.text_input("Enter your Email Address: (Compulsory) ")
    raw_message = st.text_area("Your Message: (Optional) ")

    # Add file uploader for attachment
    attachment = st.file_uploader("Upload Attachment (Compulsory)")

    subject = "New email"
    if user_email:
        subject = f"New email from {user_email}"

    # Create the email message
    message = f"From: {user_email}\n{raw_message}"

    button = st.form_submit_button("Submit")

    if button:
        # Send email with or without attachment
        if attachment is not None:
            attachment_content = attachment.getvalue()
            attachment_name = attachment.name
            contact_email(subject, message, attachment_content, attachment_name)
            st.success("Your Message Was sent Successfully. We will get back to you soonest.")
            # Reset input fields
            user_name = ""
            user_email = ""
            raw_message = ""
        else:
            contact_email(subject, message)
            st.success("Your Message Was sent Successfully. We will get back to you soonest.")
            # Reset input fields
            user_name = ""
            user_email = ""
            raw_message = ""

        # Send a confirmation message to the user's email
        if user_email and attachment is not None:
            confirmation_msg = f"Thank you for submitting '{attachment_name}'. We will get back to you soonest."
            contact_email("Submission Confirmation", confirmation_msg, attachment_content=None)


