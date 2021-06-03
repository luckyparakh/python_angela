import requests
from twilio.rest import Client
import os
import config

account_sid = config.TWILIO_ACCOUNT_SID
auth_token = config.TWILIO_AUTH_TOKEN
client = Client(account_sid, auth_token)
# Added in ENV of Pycharm Run-> Edit Config ->Python -> Choose File -> On Right Side Under Environment ->
# Environment Variable -> Click on Notepad like Icon at right most -> Popup Window -> Then '+'
my_number = os.environ.get('MY_NUMBER')

api_key = config.OWM_API_KEY
api_path = 'https://api.openweathermap.org/data/2.5/onecall'
parameter = {
    'lat': 16.30,
    'lon': 80.37,
    'appid': api_key,
    'exclude': 'daily,current'
}
request = requests.get(api_path, params=parameter)
request.raise_for_status()
data = request.json()

for i, hour in enumerate(data['hourly'][:12]):
    code = hour['weather'][0]['id']
    if code < 700:
        message = client.messages \
            .create(
            body="It may rain🌧. Bring umbrella ☂",
            from_='+13239225211',
            to=my_number
        )
        print(message.status)
        break
else:
    print("It will not rain.")
