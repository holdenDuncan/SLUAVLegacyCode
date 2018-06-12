#!/bin/bash
#Script:  detectAndSave.sh
#Created: Thursday 04/05/18 at 06:16:27 PM
#Author:  Holden Duncan
#-----------------------------#

#This script is to streamline calling the python code
#When calling have the 
#	path/to/image path/to/save/destination 
#On the command line

# Note: Currently only functions when called by 'masterScript.sh' within the master folder

python ~/interop/SLUAVProgramming/imageProcessing/detection/detectAndReturn.py $1 $2
