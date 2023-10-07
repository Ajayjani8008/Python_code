import smtplib
sender_mail = 'sender@fromdomain.com'
receiers_mail = ['receivers@todomain.com']
message = """From: From Person %s 
To:To Person %s 
Subject:Sending SMTP e-mail
This  is a test e-mail message.
""" % (sender_mail, receiers_mail)
try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender_mail, receiers_mail, message)
    print("Successfully sent email")
except Exception:
    print("Error : Unable to sent email")
