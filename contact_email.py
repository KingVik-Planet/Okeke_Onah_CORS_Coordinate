import smtplib, ssl


def contact_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "chukwukingsley56@gmail.com"
    password = "riwy cigx jwnx zdrb"
    reciever = "chukwukingsley56@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciever, message)

#
# contact_email()