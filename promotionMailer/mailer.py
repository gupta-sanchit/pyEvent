from promotionMailer.preprocess.createMail import send_mail
import pandas as pd
import smtplib
from tqdm import tqdm

data = pd.read_csv('data/test_data.csv')

sender_mail = 'ieee.bpit16@gmail.com'
sender_pass = '2018-19IeeeBpit'

with smtplib.SMTP(host='smtp.gmail.com', port=587) as s:
    s.starttls()
    s.login(sender_mail, sender_pass)

    for i in tqdm(range(len(data))):
        receiver_address = data['email'][i]

        res = send_mail(smtp_object=s, receiver_mail=receiver_address)

