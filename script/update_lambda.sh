#!/bin/bash

set -e 

echo "Delete the old lambda code"
rm -rf ./build/*

echo "Create the push weather to discord lambda zip file"
cp -r ./src/* ./build
cd ./build
zip -r9 ./pushWeatherToDiscordLambda.zip .

aws s3 cp ./pushWeatherToDiscordLambda.zip s3://discord-weather

aws lambda update-function-code --function-name pushWeatherToDiscordLambda --s3-bucket discord-weather --s3-key pushWeatherToDiscordLambda.zip
aws lambda update-function-configuration --function-name pushWeatherToDiscordLambda --handler functions.show_weather.lambda_handler
