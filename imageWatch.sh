#!/bin/bash
#Script:  imageWatch.sh
#Created: Friday 04/06/18 at 01:28:04 PM
#Author:  Holden Duncan
#-----------------------------#

# This will set up a watch on the Images folder
# that will attempt to detect ROIs and save the regions
# into the ROIs folder.

# Note: Currently only supports the addition of images
#       adding anything else will break it. This needs
#       to change once we are properly downloading metaData.

#WARNING: THIS SCRIPT MUST BE RUN BY beginWAtching.sh IN THE MASTER FOLDER
#echo -ne 'Image watch initializing...\r'
inotifywait -q  -m images/ -e create -e moved_to --format '%f' | while read FILE
    do
    sleep 20
      python ./interop/SLUAVProgramming/imageProcessing/detection/detectAndReturn.py images/$FILE images/ROIs/ &

    done
