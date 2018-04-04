#!/bin/bash
#Script: masterScript.sh
#Created Wednesday 04/04/18 at 10:12:35 AM
#Author Holden Duncan
#-----------------------------#
# This script will serve to create a
# 'one button" sort of start up function
# Also is meant to have a nice visual implementation
# so even those unfamilar with it can track what's happening

loadingBar="|------------------------------|" #loadingBars are defualt 30 len
progress=$((2))

#call this function with number after it repersenting how many blocks this progresses the program
function updateLoadingBar(){
i=$((0))
while [ $i -lt $1 ]
  do
    let "i+=1"
    loadingBar="$(echo $loadingBar | sed s/./#/$progress)"
    let "progress+=1"
    sleep .05
    echo -ne "$loadingBar\r"
  done
}


echo "Establishing Connections"
#Establish that the Connections are available

#Connections to establish
#computer to pi
./checkPi.sh && updateLoadingBar 10  &
#computer to mavlink
./checkMavLink.sh && updateLoadingBar 10  &
#computer to judges
./checkJudges.sh && updateLoadingBar 10 &

wait

#Check to see if everything connected and if so begin the processes
if [ $progress -eq 100 ]
  then
    echo -ne "\nAll Connections are valid\n"
    ./camera.sh &  #all of these scripts will be running python
    ./mavlink.sh & #scripts with proper looping and auto-restart
    ./targetSubmission.sh & #i.e. these scripts will run all
                            #competition and end when stopped with ^C
    top  echo -ne "Competition Scripts are running, use ctrl C to exit"
    wait
    
    
  else
    echo -ne "\nThere was an issue while checking connections\n"
    echo -ne "Check that all devices are on and properly addressed\n"
  fi
