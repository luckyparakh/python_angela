from datetime import *
from requests import *
import smtplib
from time import sleep

MY_LAT = 28.535517
MY_LONG = 77.391029
email = 'testlucky28@gmail.com'
password = ''
to_email = 'testlucky28@yahoo.com'


def send_mail():
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(email, to_email,
                            msg='Subject:ISS is nearby👍\n\n ISS is nearby, look up in the sky.')


def is_night_time(lat, long):
    parameter = {
        'lat': lat,
        'lng': long,
        'formatted': 0
    }
    request_s = get('https://api.sunrise-sunset.org/json', params=parameter)
    request_s.raise_for_status()
    data = request_s.json()
    sunrise_hour = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunrise_hour = (sunrise_hour + 5.5) % 24  # Added 5 hours & 30 minutes to match IST
    sunset_hour = int(data['results']['sunset'].split('T')[1].split(':')[0])
    sunset_hour = (sunset_hour + 5.5) % 24  # Added 5 hours & 30 minutes to match IST
    current_hour = datetime.now().hour
    if current_hour <= sunrise_hour or current_hour >= sunset_hour:
        return True


def is_iss_near():
    request_iss = get('http://api.open-notify.org/iss-now.json')
    request_iss.raise_for_status()
    data_iss = request_iss.json()
    iss_lat = float(data_iss['iss_position']['latitude'])
    iss_long = float(data_iss['iss_position']['longitude'])
    if MY_LAT - 5 < iss_lat < MY_LAT + 5 and MY_LONG - 5 < iss_long < MY_LONG + 5:
        return True


# If it is dark
while True:
    sleep(60)
    if is_iss_near() and is_night_time(MY_LAT,MY_LONG):
        send_mail()
    else:
        print('Waiting')
