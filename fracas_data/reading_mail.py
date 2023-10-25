import imaplib
import email

email_address = "toygar@sisray.com.tr"
password = "sisRAY102938"

def read_email(email_address, password):
    mail = imaplib.IMAP4_SSL('mail.sisray.com.tr', '993')
    mail.login(email_address, password)
    mail.select('Gelen Kutusu')
    
    status, message_data = mail.search(None, 'ALL')
    email_ids = message_data[0].split()
    
    for email_id in email_ids:
        status, msg_data = mail.fetch(email_id, '(RFC822)')
        msg = email.message_from_bytes(msg_data[0][1])
        # E-posta metnini işleme başlayın

read_email(email_address, password)