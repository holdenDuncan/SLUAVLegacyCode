# Script that checks the connection to the primary
# groundstation computer. 
# Note: this does not check the MAV connection itself

ADDR=$1

if ping -q -W 3 -c 3 192.168.0.121 -n > /dev/null 2>&1
then
#  echo "Primary GroundStation found"
  exit 0
else
 # echo "Primary has failed to connect. Check if it's on right network then try this script again"
  exit 1
fi
