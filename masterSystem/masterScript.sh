#!/bin/bash
#Script:  masterScript.sh
#Created: Friday 04/06/18 at 02:01:18 PM
#Author:  Holden Duncan
#-----------------------------#

# This will be the one script to rule them all
# and will go through and start everything needed
# for competition.
stty -echo #this is here to fix an output thing that bugs me
#Some helpful variables for use throughout the script
FAILED=0 #this variable is used so error messages may be printed
         #about what connected but aborts before continueing
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[1;36m'
YELLOW='\033[1;33m'
NC='\033[0m' #No Color
# Note: There's not much now but that will change

echo -ne "\n\n\n${BLUE}Begining Master Initialization...${NC}\n"


#-------Gather parameters-------#
# This is to avoid hard coding IPs, usernames, passwords.
# eventually this should call a script asking for the information
# on the command line.
# Note:Not sure how to really save the info between
#      script instances.

#-------Test all connections-------#
# startUp/testConns.sh
./startUp/testPi.sh
if [ $? -eq 0 ]
then
  echo -ne "${GREEN}Onboard RaspberryPi found${NC}\n"
else
  echo -ne "${RED}Onboard RaspberryPi could not be found\n"
  FAILED=1
fi

./startUp/testPrimaryGroundStation.sh
if [ $? -eq 0 ]
then
  echo -ne "${GREEN}Primary Groundstation found${NC}\n"
else
  echo -ne "${RED}Primary Groundstation could not be found\n"
  FAILED=1
fi

./startUp/testServer.sh
if [ $? -eq 0 ]
then
  echo -ne "\r${GREEN}Interop Server Log in Valid${NC}\n"
else
  echo -ne "${RED}Interop could not be found\n"
  FAILED=1
fi

if [ $FAILED -eq 1 ]
then
  echo -ne "${RED}Not all devices where able to be found\n\nAborting Program\n${NC}"
  exit 1
else
  echo -ne "${GREEN}All Devices Found${NC}\n"
  fi
sleep .5
#-------Set Up watches-------#
echo -ne "\n${YELLOW}Watches Initalizing..."
startUp/beginWatching.sh
echo -ne "${GREEN}Watches Complete${NC}\n"
#--Start all the necessary data flow--#

# ../path/to/script/mavlink.sh
# ../path/to/script/initClient.sh
# etc.

echo -ne "${BLUE}Master Initialization Complete${NC}\n\n"
sleep .5
# Start taking pictures
#./../auvsi_communications/camera/camera.sh $1
sudo sudo python3 ../auvsi_communications/camera/groundstation.py 1000 #> /dev/null 2>&1 &
groundPID=$! #will be used to kill the process later
sudo gnome-terminal --geometry 80x24+430+5 --window-with-profile=HOLD -e ./startUp/startCamera.sh > /dev/null 2>&1
#echo -ne "\n${RED}Pi is disabled in masterscript\n"

#This keeps the script going until the loop is exited
#then the clean up may take place and the program can actually end
EXIT=1
trap EXIT=0 SIGINT #sets up ^c to exit cleanly

echo -ne "${YELLOW}Use Ctrl+C to Begin ShutDown${NC}\n\n"
#Use this loop to continously show changing data
echo -ne "${BLUE}|----------System---------|${NC}\n"
echo -ne "${YELLOW}Starting Telemetry${NC}\r"
startUp/beginTelemetry.sh

while :
do
    #echo "Use Ctrl C to exit"
    #sleep 10
    if [ $EXIT -eq 0 ]
    then
    break
    fi
done
echo -ne "\n\n"
    #get key press to check against
#--Clean up, close connections, and end running jobs--#
echo -ne "\n${BLUE}Cleaning Up and Exiting Processes${NC}\n"
#script to end watches
echo -ne "${YELLOW}Ending Watches..."
startUp/endWatching.sh
echo -ne "${GREEN}All Watches Ended\n"
#close groundstation port
echo -ne "${YELLOW}Ending Ground Server..."
startUp/endGroundstation.sh $groundPID
echo -ne "${GREEN}Ground Server Ended\n"

#close connections

#check for anything still running

#Close the window
echo -ne "\n${RED}Exiting now..."
sleep 5
echo -ne "Goodbye${NC}\n"
exit 0
