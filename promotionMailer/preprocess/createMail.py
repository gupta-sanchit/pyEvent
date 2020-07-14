from email import encoders
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


sender_mail = 'ieee.bpit16@gmail.com'
sender_pass = '2018-19IeeeBpit'
import os
print(os.getcwd())

def create_message(fromaddr, toaddr):
    msg = MIMEMultipart()

    msg['From'] = fromaddr

    msg['To'] = toaddr

    msg['Subject'] = "IEEE-BPIT Career Guidance Webinar"

    with open('preprocess/body.txt') as fp:
        msg.attach(MIMEText(fp.read()))

    filename = "codeCombat.png"

    with open('media/codeCombat.png', 'rb') as fp:
        msg.attach(MIMEImage(fp.read()))

    # p = MIMEBase('application', 'octet-stream')
    #
    # p.set_payload(attachment)
    #
    # p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    #
    # msg.attach(p)
    msg.add_header('Content-Disposition', 'attachment; filename= "%s"' % filename)
    message = msg.as_string()

    return message


# def send_mail(smtp_object, receiver_mail):
#     try:
#         message = create_message(sender_mail, receiver_mail)
#         smtp_object.sendmail(sender_mail, receiver_mail, message)
#         return True
#
#     except BaseException as e:
#         print(f"Error: {e}")
#         return False

def send_mail(smtp_object, receiver_mail):

    message = create_message(sender_mail, receiver_mail)
    smtp_object.sendmail(sender_mail, receiver_mail, message)
    return True
