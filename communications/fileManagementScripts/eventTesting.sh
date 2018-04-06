#!/bin/bash
#Script:  eventTesting.sh
#Created: Thursday 04/05/18 at 12:38:59 PM
#Author:  Holden Duncan
#-----------------------------#

#This little script may be run with '&' after it
#in order to have it constantly moniter a directory

# This will activate whenever a file is created or moved into the directory


inotifywait -m ./ -e create -e moved_to --format '%f' | while read FILE
    do #reads in the variables
	#This is where the commands to run on the file
	echo $FILE
	./fileManagementScripts/detectAndSave.sh $FILE Images/targets
    done

        #This is where the commands to run on the file go
        #use '$file' for the name, for good use:
        #   mv myImage.jpeg ./ (activates the script)
        #   python turn2greyscale.py '$file'

