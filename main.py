import requests
from twilio.rest import Client
import os

OMW_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OMW_API_KEY")
account_sid = "AC81711b02eb16037aba1e3ff0909048ea"
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": 21.027763,
    "lon": 105.834160,
    "exclude": "current,minutely,daily",
    "appid": api_key
}


response = requests.get(url=OMW_Endpoint, params=weather_params)
response.raise_for_status()
data = response.json()
is_raining = False
weather_slice = data["hourly"][:12]

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 800:
        is_raining = True

if is_raining:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It is going to rain today, bring an umbrella ☔️",
        from_='+15415834773',
        to='+81 80-3720-7494'
    )



