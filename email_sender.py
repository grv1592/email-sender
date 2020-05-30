import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('C:/Users/GauravKumar/Desktop/python programs/index.html').read_text())
email = EmailMessage()

email['from'] = 'Gaurav Singh'
email['to'] = 'grv1592@gmail.com, singhgaurav949@gmail.com'
email['subject'] = 'You have won 10000000 dollars!!'

email.set_content(html.substitute({'name':'Gaurav','this':'Ludo'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('ravaginggrv@gmail.com', 'Ravageshady949')
    smtp.send_message(email)
    print('email sent!')