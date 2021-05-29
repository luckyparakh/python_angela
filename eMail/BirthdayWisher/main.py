##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

####################################################################
import smtplib
import datetime
import pandas
from random import randint

email = 'testlucky28@gmail.com'
password = '' # Set Password
to_email = 'testlucky28@yahoo.com'
df = pandas.read_csv('birthdays.csv')
dt = datetime.datetime.now()


def send_bday_mail(name):
    con = smtplib.SMTP('smtp.gmail.com')
    con.starttls()
    con.login(email, password)
    filename = f'letter_{randint(1, 3)}.txt'
    with open(f'./letter_templates/{filename}') as file:
        content = file.read().replace('[NAME]', name)
    con.sendmail(email, to_email, msg=f'Subject: Happy Birthday \n\n {content}')


for index, row in df.iterrows():
    if datetime.datetime.now().month == row.month and datetime.datetime.now().day == row.day:
        send_bday_mail(row.relative_name)
