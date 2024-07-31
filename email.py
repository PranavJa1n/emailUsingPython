from flask import Flask
app = Flask(__name__)

@app.route("/mail/<recipient_email>/<subject>/<body>")
def e_mail(recipient_email, subject, body):
    import smtplib
    from email.message import EmailMessage
    import os
    sender_email = input("Enter your Email: ")
    sender_password = input("Enter your password: ")
    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.set_content(body)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.send_message(msg)
    server.quit()
    return "Email sent successfully"

app.run(port="80",host="0.0.0.0")
