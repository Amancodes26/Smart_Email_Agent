import smtplib
from email.message import EmailMessage



def send_mail(recipient_email: str, subject: str, body: str) -> str:
    #  1. Setup email configuration
    SENDER_EMAIL = "amansngh8586@gmail.com"
    SENDER_PASSWORD = "vkhz jjxq aeev aoxz"  # Do not use your primary password; use an App Password

    # 2. Build the email message
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = recipient_email
    msg.set_content(body)

    # 3. Establish a secure SMTP connection and send
    try:
        # Use standard SMTP with port 587
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.ehlo()            # Identify yourself to the server
            server.starttls()        # Upgrade the connection to secure TLS encryption
            server.ehlo()            # Re-identify yourself over encrypted connection
            
            # Log in and dispatch email
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)

        return "Email sent successfully!"
    except Exception as e:
        return f"An error occurred: {e}"
