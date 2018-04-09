#!/bin/bash
#Script:  endWatching.sh
#Created: Monday 04/09/18 at 10:08:07 AM
#Author:  Holden Duncan
#-----------------------------#

# This is a clean up script for ending
# all the inotifywait commands running in the background.

# Note: As more watches are made this script needs to be updated.

ps -aux | grep imageWatch.sh
killall imageWatch.sh inotifywait
