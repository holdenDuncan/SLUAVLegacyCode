#!/bin/bash
#Script:  ROIwatch.sh
#Created: Tuesday 04/10/18 at 12:09:24 PM
#Author:  Holden Duncan
#-----------------------------#

# This script is to set up the appropriate watch on the ROI folder

#WARNING: THIS SCRIPT MUST BE RUN BY beginWAtching.sh IN THE MASTER FO$
#echo -ne 'ROI watch initializing...\r'
inotifywait -q  -m Images/ROIs/ -e create -e moved_to --format '%f' | while$
    do

      ../communications/fileManagementScripts/classifyAndMove.sh Images/$

    done


