import datetime as dt
import smtplib
import pandas as pd
from random import choice

my_email = ""
password = ""

item_to_replace = "[NAME]"
data = pd.read_csv("birthdays.csv")
letters = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]

date = dt.datetime.now()
month = date.month
day = date.day

contacts = data[(data.day == day) & (data.month == month)]

for i, value in contacts.iterrows():
    name = value[0]
    email = value[1]
    month = value[3]
    day = value[4]
    letter = choice(letters)
    with open(letter, "r") as file_open:
        replaced_letter = file_open.read().replace(item_to_replace, name)
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=email,
                            msg=f"Subject: Happy Birthday\n\n{replaced_letter}")
