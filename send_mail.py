import smtplib
from email.message import EmailMessage
import ssl

import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

sender = os.getenv('SENDER_EMAIL')
password = os.getenv('SENDER_EMAIL_PASSWORD')
receiver = os.getenv('RECIEVER_EMAIL')


subject = "SMTP e-mail test"
body = "This is a test e-mail message."

em = EmailMessage()
em['from'] = sender
em['to'] = receiver
em['subject'] = subject
em.set_content(body)

# Establish a connection
context = ssl.create_default_context()
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    # Start a secure TLS connection
    smtp.starttls(context=context)
    smtp.login(sender, password)
    smtp.send_message(em)