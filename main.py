import smtplib
import random
import datetime as dt

from dotenv import dotenv_values

config = dotenv_values('.env')

MY_EMAIL = config['MY_EMAIL']
MY_PASSWORD = config['MY_PASSWORD']
now = dt.datetime.now()
if now.weekday() == 1:  # monday quotes
    with open('quotes.txt', 'r') as quotes:
        content = quotes.readlines()
        quote_of_the_day = random.choice(content)

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f'Subject:Test mail\n\n {quote_of_the_day}'
        )
