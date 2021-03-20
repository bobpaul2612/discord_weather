#!/bin/bash

set -e 

echo "Delete the old dependence layer"
rm -rf ./layer/*

echo "Create the dependence layer zip file"
pip install --target ./layer/python -r ./requirement.txt
cd ./layer
zip -r9 ./pushWeatherToDiscordLayer.zip ./python

echo "Store the dependence layer to S3"
aws s3 cp ./pushWeatherToDiscordLayer.zip s3://discord-weather

echo "Update the layer version"
layer_resp=$(aws lambda publish-layer-version \
                --layer-name pushWeatherToDiscordLayer \
                --content S3Bucket=discord-weather,S3Key=pushWeatherToDiscordLayer.zip \
                --compatible-runtimes python3.8)

layer_version=$(echo "$layer_resp" | jq -r '.LayerVersionArn')

echo "Set the lastest layer version to lambda function"
aws lambda update-function-configuration --function-name pushWeatherToDiscordLambda --layers $layer_version



