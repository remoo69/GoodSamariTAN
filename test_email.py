import smtplib

try:
    # SMTP configuration
    smtp_server = 'smtp.gmail.com'
    port = 587
    sender_email = 'samaritan.dev@gmail.com'
    password = 'gtfw xvdv kasz aetv'  # Replace with your Gmail app password

    # Establish connection to the SMTP server
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()  # Start TLS encryption
    server.login(sender_email, password)  # Login to the SMTP server

    # Email details
    recipient_email = 'ortiaga.jcee30@gmail.com'  # Replace with your test email
    subject = 'Test Email'
    body = 'This is a test email sent using Python and Gmail SMTP.'

    # Compose email
    message = f"Subject: {subject}\n\n{body}"
    
    # Send email
    server.sendmail(sender_email, recipient_email, message)
    print("Email sent successfully!")

    # Close connection
    server.quit()

except Exception as e:
    print(f"Failed to send email. Error: {e}")
