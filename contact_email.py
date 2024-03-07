import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import streamlit as st
import datetime

# create_confirmation_message function to return HTML-formatted confirmation message
def create_confirmation_message(reference_number):
    confirmation_message = f"""<html><body>
    <div style='text-align: center; background-color: lightgreen; border-radius: 10px; padding: 10px;'>
        <h1 style='color: blue;'>Submission Confirmation</h1>
        <p>Thank you for submitting your Data. We will get back to you soonest.</p>
        <p><strong>Confirmation Email:</strong> You will receive a confirmation email once your submission is successfully received. Please allow 3 to 15 minutes for this.</p>
        <p><strong>Feedback Delivery:</strong> Expect to receive feedback on your data within 4 to 5 hours of submission.</p>
        <p><strong>No Feedback?:</strong> In the rare event that you don't receive feedback after 5 hours, please don't hesitate to contact us through our email: okekeonahcorsprocessingunn@gmail.com.</p>
        <p><strong>24-hour Response:</strong> If you encounter any issues or have questions, rest assured, we'll provide you with feedback within 24 hours.</p>
        <p>Thank you once again for choosing us. Have a wonderful and productive time!</p>
    </div>
    </body></html>"""
    return confirmation_message

# Adjusted contact_email function to send HTML-formatted confirmation message
def contact_email(subject, message, attachment_data, attachment_filename, sender_email, user_email):
    sender_email = "okekeonahcorsprocessingunn@gmail.com"  # Receiver's email address
    password = st.secrets["pwd"]  # Sender's email password
    host = "smtp.gmail.com"
    port = 465

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Create a multipart message
    email_message = MIMEMultipart()
    email_message["From"] = sender_email
    email_message["To"] = user_email  # Set recipient to user_email
    email_message["Subject"] = subject

    # Add message body as HTML
    confirmation_message = create_confirmation_message(attachment_filename)
    confirmation_message += f" Thank you for Submitting your CORS Data to Okeke_Onah GNSS CORS Processing Center, Your reference number is '{attachment_filename}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')}', This reference Number will be used to track your data to ensure it get back to you."
    email_message.attach(MIMEText(confirmation_message, "html"))  # Set content type to HTML

    # Add attachment if provided
    if attachment_data is not None:
        attachment = MIMEApplication(attachment_data, Name=attachment_filename)
        attachment["Content-Disposition"] = f"attachment; filename={attachment_filename}"
        email_message.attach(attachment)

    try:
        # Connect to SMTP server and send email to both receiver and sender
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(sender_email, password)
            recipients = [user_email, sender_email]  # Include sender's email in recipients list
            server.sendmail(sender_email, recipients, email_message.as_string())

    except Exception as e:
        st.error(f"An error occurred while sending the email: {e}")
