import streamlit as st
from contact_email import contact_email

# st.markdown("<h1 style='text-align: center; color: blue;'>Okeke_Onah GNSS CORS Processing Center</h1>",
#             unsafe_allow_html=True)
st.markdown("""
    <div style='text-align: center; background-color: lightgreen; border-radius: 10px; padding: 10px;'>
        <h1 style='color: blue;'>Okeke_Onah GNSS CORS Processing Center</h1>
    </div>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: blue;'>Upload the CORS Data Here:</h2>",
            unsafe_allow_html=True)
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

######################################################################################################
######################################################################################################

import datetime
import streamlit as st
from contact_email import contact_email

# Function to generate reference number
def generate_reference_number(file_name):
    current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    return f"{file_name}_{current_time}"

with st.form(key="email_forms"):
    user_email = st.text_input("Enter your Email Address: (Compulsory)")

    attachment = st.file_uploader("Upload Attachment (Compulsory)")

    subject = "Data Submission : Okeke_Onah GNSS CORS Processing Center"  # Set the default subject
    # if user_email:
    #     subject = f"Okeke_Onah GNSS CORS Processing Center - New email from {user_email}"  # Update the subject if email is provided

    message = f"From: {user_email}"

    if not user_email:
        st.error("Please enter your email address.")
    if not attachment:
        st.error("Please upload an attachment.")

    submit_button_clicked = st.form_submit_button("Submit")

    if submit_button_clicked:
        if user_email and attachment:
            if attachment is not None:
                attachment_content = attachment.getvalue()
                attachment_name = attachment.name
                reference_number = generate_reference_number(attachment_name)
                # confirmation_msg = f"Thank you for submitting '{attachment_name}'. Your reference number is '{reference_number}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')}'. We will get back to you soonest."
                # contact_email("Data Submission Confirmation", confirmation_msg, None, None, "okekeonahcorsprocessingunn@gmail.com", user_email)

                contact_email(subject, message, attachment_content, attachment_name, "okekeonahcorsprocessingunn@gmail.com", user_email)
                st.success("Your Data Was sent Successfully. We will get back to you soonest.")






            # else:
            #     reference_number = generate_reference_number("NoAttachment")
            #     confirmation_msg = f"Thank you for submitting your message. Your reference number is '{reference_number}'. We will get back to you soonest."
            #     contact_email("Data Submission Confirmation", confirmation_msg, None, None, "okekeonahcorsprocessingunn@gmail.com", user_email)
            #
            #     contact_email(subject, message, None, None, "okekeonahcorsprocessingunn@gmail.com", user_email)
            #     st.success("Your Message Was sent Successfully. We will get back to you soonest.")
