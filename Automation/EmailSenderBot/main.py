import smtplib
import ssl
from email.message import EmailMessage

subject = "Email From Python"
body = "This is a test email from Python!"
sender_email = input("Please enter your email address: ")
receiver_email = input("Please enter the email address of the recipient: ")
password = input("Enter your email password: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</p>
    </body>
</html>
"""

message.add_alternative(html, subtype="html")

context = ssl.create_default_context()

try:
    print("Sending Email...")
    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    
    print("Email sent successfully!")
except Exception as e:
    print(f"An error occurred while sending the email: {str(e)}")
