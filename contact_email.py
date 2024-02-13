import smtplib, ssl
import streamlit as st

st.title("Okeke_Onah GNSS CORS processing center")
content = """Hello, Thank you for choosing us to handle your data. 
Please follow these simple steps for a seamless experience:

1. Enter Your Name: Provide your full name so we can address you properly.

2. Enter Your Email: Double-check your email for accuracy. Any errors might result in a delay or failure to receive feedback.

3. Short Message or Remarks: If you have any additional comments or remarks, feel free to include them here.

4. Upload Your Data: Select the file you wish to upload for processing.

5. Submit: Once you've completed the above steps, hit the submit button.

6. Confirmation Email: You will receive a confirmation email once your submission is successfully received. Please allow 3 to 15 minutes for this.

7. Feedback Delivery: Expect to receive feedback on your data within 4 to 5 hours of submission.

8. No Feedback?: In the rare event that you don't receive feedback after 5 hours, please don't hesitate to contact us.

9. 24-hour Response: If you encounter any issues or have questions, rest assured, we'll provide you with feedback within 24 hours.

Thank you once again for choosing us. Have a wonderful and productive day!
"""
st.info(content)


import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from keys import user, pwd


def contact_email(subject, message, attachment_content=None, attachment_name=None):
    host = "smtp.gmail.com"
    port = 465
    username = user
    password = ${{ secrets.KEYS }}
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
