from utils.api import generator_response
from services.weather_service import Weather_Service


def lambda_handler(event, context):
    resp = {}

    try: 
        weather_service = Weather_Service()
        weather_service.push_weather_to_discord_channel()
        resp = generator_response(200, "OK !")
    except Exception:
        resp = generator_response(500, "Something Error ! ! !")

    return resp