import requests
import json
import re 
from env import env  

class Weather_Service():
    
    def push_weather_to_discord_channel(self):
        weather_message = self._get_12h_weather()

        payload = {
            "username": "竹塘鄉天氣 - Alex",
            "content": weather_message
        }

        requests.post(env.DISCORD_WEBHOOK, json=payload)

    def _get_12h_weather(self):
        payload = {
            "Authorization": env.CWB_AUTHORIZATION,
            "locationName": "竹塘鄉",
            "elementName": ["WeatherDescription"]
        }

        resp = requests.get("https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-019", 
            params=payload)

        resp_message = resp.json()["records"]["locations"][0]["location"][0]["weatherElement"][0]["time"][0]
        
        startTime = resp_message["startTime"]
        endTime = resp_message["endTime"]
        weatherDescription = resp_message["elementValue"][0]["value"].split("。")

        weather_message = f"竹塘鄉 12 小時天氣預報\n" + \
            f"```\n" + \
            f"時間：{startTime} ~ {endTime}：\n" + \
            f"天氣狀況：{weatherDescription[0]}\n" + \
            f"氣溫變化：{self._trans_temperature(weatherDescription[2])}\n" + \
            f"降雨機率：{weatherDescription[1]}\n" + \
            f"體感溫度：{weatherDescription[3]}\n" + \
            f"```"

        return weather_message

    def _trans_temperature(self, temp):
        temp_num = re.findall(r"\d+\.?\d*", temp)
        new_temp = f"{temp_num[0]}°C ~ {temp_num[1]}°C"
        return new_temp

# if __name__ == "__main__":
#     weather = Weather_Service()
#     weather._get_12h_weather()
    
