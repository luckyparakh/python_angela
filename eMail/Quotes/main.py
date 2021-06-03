import smtplib
import datetime as dt
from random import choice
import config

email = config.EMAIL
password = config.PASSWORD
to_email = config.TO_EMAIL
sub = "Quote of Day"
day = dt.datetime.now().weekday()

if day == 5:
    with open('quotes.txt', 'r') as file:
        quotes = file.readlines()
        quote = choice(quotes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(from_addr=email,
                            to_addrs=to_email,
                            msg=f'Subject:{sub}\n\n{quote}')
