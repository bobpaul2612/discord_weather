#!/bin/bash

set -e 

echo "update all service"
sh ./script/update_lambda.sh
sh ./script/update_layer.sh