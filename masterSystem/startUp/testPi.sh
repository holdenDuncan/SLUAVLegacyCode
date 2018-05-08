#!/bin/bash
# Script that checks the connection to the rpi
# and the camera's picture taking abilites

ADDR=$1

if ping -q -W 3 -c 3 192.168.0.164 -n > /dev/null 2>&1
then
  #Pi was found
  exit 0
else
 # echo "Pi has failed to connect. Check if it's on then try this script again"
  exit 1
fi
