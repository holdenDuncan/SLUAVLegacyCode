#!/bin/bash
#Script:  masterScript.sh
#Created: Friday 04/06/18 at 02:01:18 PM
#Author:  Holden Duncan
#-----------------------------#

# This will be the one script to rule them all
# and will go through and start everything needed
# for competition.

# Note: There's not much now but that will change

#-------Gather parameters-------#
# This is to avoid hard coding IPs, usernames, passwords.
# eventually this should call a script asking for the information
# on the command line.
# Note:Not sure how to really save the info between
#      script instances.

#-------Test all connections-------#
# startUp/testConns.sh

#-------Set Up watches-------#
echo 'Setting up watches'
startUp/beginWatching.sh
echo 'Watches Complete'
#--Start all the necessary data flow--#
# ../path/to/script/mavlink.sh
# ../path/to/script/initClient.sh
# etc.

#--Clean up, close connections, and end running jobs--#
#script to end watches
#close connections
#check for anything still running

