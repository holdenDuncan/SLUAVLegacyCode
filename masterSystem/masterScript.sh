#!/bin/bash
#Script:  masterScript.sh
#Created: Friday 04/06/18 at 02:01:18 PM
#Author:  Holden Duncan
#-----------------------------#

# This will be the one script to rule them all
# and will go through and start everything needed
# for competition.

# Note: There's not much now but that will change

echo -ne 'Begining Master Initialization...\n\n'

#-------Gather parameters-------#
# This is to avoid hard coding IPs, usernames, passwords.
# eventually this should call a script asking for the information
# on the command line.
# Note:Not sure how to really save the info between
#      script instances.

#-------Test all connections-------#
# startUp/testConns.sh

#-------Set Up watches-------#
startUp/beginWatching.sh
echo -ne 'Watches Complete\n\n'
#--Start all the necessary data flow--#
# ../path/to/script/mavlink.sh
# ../path/to/script/initClient.sh
# etc.

echo -ne 'Master Initialization Complete\n\n'

#--Clean up, close connections, and end running jobs--#
#script to end watches
#close connections
#check for anything still running

