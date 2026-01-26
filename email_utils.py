
# utils.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def send_selection_email(to_email, role):
    # Your email credentials
    sender_email = "your_email@gmail.com"      # <-- replace with your email
    sender_password = "your_app_password"      # <-- use app password if Gmail
    subject = f"Congratulations! Selected for {role}"
    body = f"Dear Candidate,\n\nYou are selected for the role of {role}. Congratulations!\n\nBest Regards,\nTeam"
    # Create email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    # Send email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
    except Exception as e:
        raise e
