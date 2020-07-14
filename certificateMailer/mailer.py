import pandas as pd
import smtplib
from tqdm import tqdm

from certificateMailer.credentials import sender_mail, sender_pass
from certificateMailer.preprocess.createMail import send_mail


data = pd.read_csv('data/test_data.csv')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as s:
    s.starttls()
    s.login(sender_mail, sender_pass)

    for i in tqdm(range(len(data))):
        try:

            receiver_address = data['email'][i]
            certificate_id = data['certificateID'][i]
            attachment = open(f"certificates/{certificate_id}.pdf", 'rb')

            res = send_mail(smtp_object=s, receiver_mail=receiver_address, fp=attachment)

        except BaseException as e:
            print(f"error in certificate id: {certificate_id}")
            print(f"error: {e}")

