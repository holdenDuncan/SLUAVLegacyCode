#!/bin/bash
#Script:  beginWatching.sh
#Created: Friday 04/06/18 at 01:58:00 PM
#Author:  Holden Duncan
#-----------------------------#

# This script is to start all of the watch scripts
# for the directories and will require updateing as
# new processes are completed and introduced

#echo -ne 'Watches Initalizing...\n'
./imageWatch.sh &
./submitWatch.sh &
#startUp/roiWatch.sh &
