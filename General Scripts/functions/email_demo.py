import smtplib

server =smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()

server.login("wn@gmail.com", "samco@78718")

server.sendmail("example@gmail.com", "sam.1234@gmail.com", "Mail sent from Python code")
print("Mail sent!")