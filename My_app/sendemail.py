import smtplib
#import sendgrid
import os
#from sendgrid.helpers.mail import Mail, Email, To, Content
SUBJECT = "Inventory Check"
s = smtplib.SMTP('smtp.gmail.com', 587)


def sendmail(TEXT,email):
    print("sorry we cant process your candidature")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    #s.login("bruce.hulk91@gmail.com", "bruceishulk")
    s.login("retinvmgmt@gmail.com","retailinventorymgmt")
    message  = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    #s.sendmail("bruce.hulk91@gmail.com", email, message)
    s.sendmail("retinvmgmt@gmail.com", email, message)
    s.quit()


"""
def sendmail(dum,email):
    #print("sorry we cant process your candidature")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    #s.login("bruce.hulk91@gmail.com", "bruceishulk")
    s.login("retinvmgmt@gmail.com","retailinventorymgmt")
    #message  = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    msg = ''
    for i in range(len(dum)):
        msg += dum[i]+'\n\n'
    
    message  = 'Subject: {}\n\n{}'.format(SUBJECT, msg)
    #s.sendmail("bruce.hulk91@gmail.com", email, message)
    s.sendmail("retinvmgmt@gmail.com", email, message)
    s.quit()

"""
"""
def sendgridmail(user,TEXT):
    sg = sendgrid.SendGridAPIClient('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')
    from_email = Email("retinvmgmt@gmail.com")  # Change to your verified sender
    to_email = To(user)  # Change to your recipient
    subject = "Sending with SendGrid is Fun"
    content = Content("text/plain",TEXT)
    mail = Mail(from_email, to_email, subject, content)

    # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()
    # Send an HTTP POST request to /mail/send
    response = sg.client.mail.send.post(request_body=mail_json)
    print(response.status_code)
    print(response.headers)
"""    

