# discord_weather
Show weather to discord channel

How to use?
1. Create an aws lambda function "pushWeatherToDiscordLambda" 
2. Create an aws lambda layer "pushWeatherToDiscordLayer" 
3. Create an aws s3 bucket "discord-weather"
4. Add an env dictionary in src/
```
src
├─ env
|  └─ __init__.py
|  └─ env.py
```
5. In the env.py add code
```python
DISCORD_WEBHOOK = "your-discord-webhook-link"
CWB_AUTHORIZATION = "your-cwb-authorization-link"
```
6. Update lambda function and layer by 
```
$ sh ./script/update_service.py
```

* If you only want to update lambda function or layer
```
$ sh ./script/update_lambda.py
$ sh ./script/update_layer.py
```