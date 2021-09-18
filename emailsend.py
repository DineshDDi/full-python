import ssl, smtplib

port = 465

email = input("enter your email : ")
password = input("enter your password : ")

recipient = input("enter the To address : ")

subject = input("enter your subject : ")

text = input("Type your email here : ")

message = "Subject: {}\n\n{}".format(subject, text)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com",port,context=context) as servers:
        servers.login(email,password)
        servers.sendmail(email, recipient,message)




