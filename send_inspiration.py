import os
import smtplib

from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS ='godfrey.dlamini@umuzi.org'
PASSWORD ='nZHCzjs5cqy9khT8'
Email_To = 'godfreydlamini596@gmail.com'

def get_contacts(filename):
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails

def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def main():
    names, emails = get_contacts('contactlist.txt') 
    message_template = read_template('message.txt')
    s = smtplib.SMTP(host='smtp-relay.sendinblue.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)    
    for name, email in zip(names, emails):
        msg = MIMEMultipart()      
        message = message_template.substitute(PERSON_NAME=name.title())
        print(message)
        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Subject']="This is TEST"
        msg.attach(MIMEText(message, 'plain'))
        s.send_message(msg)
        del msg
    s.quit()
if __name__ == '__main__':
    main()