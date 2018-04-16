#!/bin/bash
#Script:  cleanUp.sh
#Created: Monday 04/09/18 at 12:50:53 PM
#Author:  Holden Duncan
#-----------------------------#

# This script is to scrub clean the directories of images
# for the sake of organization.

# Works by taking all the images with '.jpg' or '.jpeg'
# and deleting them. If you're worried about keeping images
# make sure they are saved somewhere else before running this.

# Note: This script also runs the endWatches.sh to make Holden's life easier
#         Also, this only works when called and ran within the master folder

find images/  -type f \( -name "*.jpg" -o -name "*.jpeg" \) -delete
find images/ROIs/ -type f \( -name "*.jpg" -o -name "*.jpeg" \) -delete
#find Images/ROIs/Targets -type f -iname \*.jpg -delete
#find Images/ROIs/Garbage -type f -iname \*.jpg -delete
#find Images/ROIs/Targets -type f -iname \*.jpg -delete
#find Images/ROIs/Targets/Submit -type f -iname \*.jpg -delete

startUp/endWatching.sh
