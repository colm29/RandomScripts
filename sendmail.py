from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

template = Template(Path('template.html').read_text())

message = MIMEMultipart()
message['from'] = 'somebody'
message['to'] = 'xxx@gmail.com'
message['subject'] = 'This is a test'
body = template.substitute({'name': 'John'})
message.attach(MIMEText('Body', 'plain'))
message.attach(MIMEImage(Path('pic.jpg').read_bytes()))

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('somebody@gmail.com', 'ghggvghf585')
    smtp.send_message(message)
    print('Sent...')
