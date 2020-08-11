# In this project we will send and receive emails , using G-mail
# 12:04--> continue from here
import smtplib
username = '*********'
password = '**********'
def send_mail(text = 'Email Body' , subject = 'This is the mail subject' , receiver_mail = [] , sender_mail = '*****'):
    #isinstance() will check if a given object or a variable is of a certain type.
    #If the condition is true, it does nothing and your program just continues to execute. 
    # But if the assert condition evaluates to false, 
    # it raises an AssertionError exception with an optional error message.
    assert isinstance(receiver_mail = list)
    
    # Start the smtp server
    # server = smtplib.SMTP()
    # server.ehlo() # config to run by default
    # server.starttls


    with smtplib.SMTP(host='smtp.gmail.com' , port=547) as server:
        server.ehlo()
        server.starttls
        server.login(username , password)
        server.sendmail(sender_mail , receiver_mail , msg_str)
     