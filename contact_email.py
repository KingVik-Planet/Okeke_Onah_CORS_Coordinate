import smtplib, ssl
import streamlit as st
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


headers= {
    "authorization": st.secrets["pwd"],
    "content-type": "application/josn"
}

def contact_email(subject, message, attachment_content=None, attachment_name=None):
    host = "smtp.gmail.com"
    port = 465
    username = "chukwukingsley56@gmail.com"
    # password = me("xxx")
    password = st.secrets["pwd"]
    sender = username
    receiver = "chukwukingsley56@gmail.com"
    context = ssl.create_default_context()

    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    # Attach message body
    body = MIMEText(message)
    msg.attach(body)

    if attachment_content is not None:
        # Attach the attachment content
        attachment = MIMEApplication(attachment_content)
        attachment.add_header("Content-Disposition", "attachment", filename=attachment_name)
        msg.attach(attachment)

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(sender, receiver, msg.as_string())



