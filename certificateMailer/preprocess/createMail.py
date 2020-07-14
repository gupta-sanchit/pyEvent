from certificateMailer.credentials import sender_mail

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def create_message(fromaddr, toaddr, attachment):
    msg = MIMEMultipart()

    msg['From'] = fromaddr

    msg['To'] = toaddr

    msg['Subject'] = "IEEE-BPIT Code Combat"

    with open('preprocess/body.txt') as fp:
        msg.attach(MIMEText(fp.read()))

    filename = "ieeeBpitCodeCombatCertificate.pdf"

    p = MIMEBase('application', 'octet-stream')

    p.set_payload(attachment.read())

    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(p)
    message = msg.as_string()

    return message


def send_mail(smtp_object, receiver_mail, fp):
    try:
        message = create_message(sender_mail, receiver_mail, fp)
        smtp_object.sendmail(sender_mail, receiver_mail, message)
        return True

    except BaseException as e:
        print(f"Error: {e}")
        return False
