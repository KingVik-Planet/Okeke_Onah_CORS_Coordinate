# import smtplib, ssl
# import streamlit as st
# import smtplib
# import ssl
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.application import MIMEApplication
#
#
# headers= {
#     "authorization": st.secrets["pwd"],
#     "content-type": "application/josn"
# }
#
# def contact_email(subject, message, attachment_content=None, attachment_name=None):
#     host = "smtp.gmail.com"
#     port = 465
#     username = "chukwukingsley56@gmail.com"
#     # password = me("xxx")
#     password = st.secrets["pwd"]
#     sender = username
#     receiver = "chukwukingsley56@gmail.com"
#     context = ssl.create_default_context()
#
#     msg = MIMEMultipart()
#     msg["From"] = sender
#     msg["To"] = receiver
#     msg["Subject"] = subject
#
#     # Attach message body
#     body = MIMEText(message)
#     msg.attach(body)
#
#     if attachment_content is not None:
#         # Attach the attachment content
#         attachment = MIMEApplication(attachment_content)
#         attachment.add_header("Content-Disposition", "attachment", filename=attachment_name)
#         msg.attach(attachment)
#
#     with smtplib.SMTP_SSL(host, port, context=context) as server:
#         server.login(username, password)
#         server.sendmail(sender, receiver, msg.as_string())


import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import streamlit as st
import datetime

def contact_email(subject, message, attachment_content, attachment_name, user_email):
    sender_email = "chukwukingsley56@gmail.com"  # Sender's email address
    receiver_email = "chukwukingsley56@gmail.com"  # Receiver's email address
    password = st.secrets["pwd"]  # Sender's email password
    host = "smtp.gmail.com"
    port = 465

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Create a multipart message
    email_message = MIMEMultipart()
    email_message["From"] = sender_email
    email_message["Subject"] = subject

    # Add message body
    email_message.attach(MIMEText(message, "plain"))

    # Add attachment if provided
    if attachment_content is not None:
        attachment = MIMEApplication(attachment_content, Name=attachment_name)
        attachment["Content-Disposition"] = f"attachment; filename={attachment_name}"
        email_message.attach(attachment)

    try:
        # Connect to SMTP server and send email to receiver
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, email_message.as_string())

        # Send confirmation email to the user's email
        if user_email:
            confirmation_subject = "Submission Confirmation"
            confirmation_message = f"Thank you for submitting your message. We will get back to you soonest."
            confirmation_message += f" Your reference number is '{attachment_name}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')}'."

            with smtplib.SMTP_SSL(host, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, user_email, confirmation_message)

        # Send email to sender
        if attachment_content is not None:
            sender_message = f"Thank you for submitting your message. We will get back to you soonest."
            sender_message += f" Your reference number is '{attachment_name}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')}'."

            email_message = MIMEMultipart()
            email_message["From"] = sender_email
            email_message["Subject"] = "Submission Confirmation"
            email_message.attach(MIMEText(sender_message, "plain"))

            with smtplib.SMTP_SSL(host, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, sender_email, email_message.as_string())

    except Exception as e:
        st.error(f"An error occurred while sending the email: {e}")
