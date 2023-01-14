import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# "darkberrydrpepper@gmail.com",
# xqanxiellplbdfre
# variables for emails
# mime multipart is used for sending text and non-text emails/attachments
email_sender = "Brodie.Liverman@gmail.com"
email_list = ["Brodie.Liverman@gmail.com", "gangsquad694202@gmail.com"]
# gets value of environmental variable
email_password = os.getenv('EMAIL_PASSWORD')

subject = "TEST EMAIL THROUGH SCRIPT"
body = """
You are being hacked

*This email was sent through python*

"""
#sets up the attachment to be added
#\' is an escape sequence for a quotation mark

file_location = r'C:\Users\Brodie Liverman\Documents\GitHub\Python-Projects\Python Scripts\art ex.JPG'
filename = os.path.basename(file_location)
attachment = open(file_location, "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', f'attachment; filename= {filename}')

#sends 1 email per person using the for loop
for email_list in email_list:
    em = MIMEMultipart()
    em['From'] = email_sender
    em['To'] = email_list
    em["Subject"] = subject
    em.attach(MIMEText(body, 'plain'))

    #adds attachment to email
    em.attach(part)

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        # this logs in and actually send the email
        #used for security purposes
        smtp.starttls()
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_list, em.as_string())
