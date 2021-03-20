import requests
import json
from env import env 

class Weather_Service():
    
    def push_weather_to_discord_channel(self):
        weather_message = self._get_12h_weather()

        payload = {
            "username": "Weather Bot",
            "content": weather_message
        }

        requests.post(env.DISCORD_WEBHOOK, json=payload)

    def _get_12h_weather(self):
        payload = {
            "Authorization": env.CWB_AUTHORIZATOIN,
            "locationName": "竹塘鄉",
            "elementName": ["WeatherDescription"]
        }

        resp = requests.get("https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-019", 
            params=payload)

        resp_message = resp.json()["records"]["locations"][0]["location"][0]["weatherElement"][0]["time"][0]
        
        startTime = resp_message["startTime"]
        endTime = resp_message["endTime"]
        weatherDescription = resp_message["elementValue"][0]["value"]

        weather_message = f'{startTime} 到 {endTime} 的天氣狀況為：{weatherDescription}'

        return weather_message

if __name__ == "__main__":
    weather = Weather_Service()
    weather.push_to_discord_channel()
    
