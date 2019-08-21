import smtplib
import sys

eml=sys.argv[1]
passwd=sys.argv[2]

class Gmail:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.server = 'smtp.gmail.com'
        self.port = 587
        session = smtplib.SMTP(self.server, self.port)        
        session.ehlo()
        session.starttls()
        session.ehlo
        session.login(self.email, self.password)
        self.session = session
    def send_message(self, subject, body):
        ''' This must be removed '''
        headers = [
            "From: " + self.email,
            "Subject: " + subject,
            "To: " + self.email,
            "MIME-Version: 1.0",
            "Content-Type: text/html"]
        headers = "\r\n".join(headers)
        self.session.sendmail(
            #self.email,
            #self.email,
            'info@eipoteka.az',
            eml,
            headers + "\r\n\r\n" + body)


#gm = Gmail('fariz.muradov@cybernet.az', '')
#gm.send_message('Password', 'Dear User '+str(eml)+'\n\rPlease use set your password for http://gmail.cybernet.az.az\n\r'+'Your default password is : '+str(passwd))


import smtplib
from email.mime.text  import MIMEText
 
smtpadresi = "smtp.gmail.com"
smtpport = 587
kullaniciadi = "info@eipoteka.az"
sifre = "Admin12345"
 
gonderilecekadres = ["babakmammadov15@gma"]
konu = "Python ile Mail Göndermek"
icerik = """
 
İÇERİĞİNİZİ HTML OLARAK GİRMENİZ GEREKİYOR. TABİ NORMALDE GİREBİLİRSİNİZ. AMA RENK, ALTA KAYDIRMA, İTALİK GİBİ ÖZELLİKLERİ HTML OLARAK HAZIRLAYIP GÖNDERMELİSİNİZ.
 
"""
 
mail = MIMEText(icerik, "html", "utf-8")
mail["From"] = kullaniciadi
mail["Subject"] = konu
mail["To"] = ",".join(gonderilecekadres)
 
mail = mail.as_string()
 
print("Lütfen bekleyiniz. Mail gönderiliyor..")
 
s = smtplib.SMTP(smtpadresi,smtpport)
s.starttls()
s.login(kullaniciadi, sifre)
s.sendmail(kullaniciadi, gonderilecekadres, mail)
print("Mail gönderildi.")



import smtplib
import ssl
import sys

port = 465  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "info@eipoteka.az"
receiver_email = "info@eipoteka.az"
password = "Admin12345"
message = """\
Subject: Hi there

This message is sent from Python."""
print "Salamm"
context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)