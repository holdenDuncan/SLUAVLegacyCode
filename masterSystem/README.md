This directory is to be used for the final structure of the program to
be run at competition. General Rules for this directory:

-Do not remove or move directories as scripts might
    rely on a specific structure of directories
    i.e. when shipping files around to certain destinations

-As far as I am aware these scripts are linux specific and 
    also require a number of dependencies to be installed. So
    the code here is likely to not function on other machines than
    Holden's personal machine (sorry not sorry) and the secondary ground
    station computer to be at competition (Would have been the lab's grey
    one but it's broken currently). Unless the machine is running Ubuntu
    and has all necessary dependencies. (See below)

-If addition dependencies are ever required please up update the 
    dependencies.txt so others can check there to see if they have everything
    required.

-If anyone dislikes this hierarchy complain to Holden and the team
    can communicate on how to better structure it and then also update
    hard coded paths within the scripts.

-Keep source code in the proper directory. To access source code 
    use ../path/to/file in order to step out of this directory.
    (Use /../ in order to step out as many times as needed)

#-----------The file structure------------#

               masterSystem
 This should contain just one script to rule them all
 i.e. this starts everything needed for the competition
                    /\
                   /  \
                  /    \         
           startUp      Images
      initialization      raw downloaded images
    scripts like all            are processed when they enter here     
    the needed watch           /\
    scripts and               /  \
    telemetry etc.           /    \
                            /      \
                     Metadata       ROIs
            Contains the metadata        Contains cropped images
          of the ROI as a .json     of possible targets based
          that may be copied        on the detection scripts.
          down later if the ROI     Classification is run on
          is classified as a        files that enter here.       
          target                             /\
                                            /  \
                                           /    \
                                          /      \
				   Garbage	  Targets
                            ROI's rejected          An image that makes it here
                            as non-targets        has been classified and has a
                            kept to help with     similarly named .json of data.
                            debugging and to      and once here it is checked to 
                            see what's being      see if it is a duplicate of a 
                            rejected              previously submitted target and 
                                                  if not it is submitted.
                                                              \
                                                               \
                                                                \
                                                                 \
                                                                  Submitted
                                                                    Images placed here will be
                                                                  submitted along with their .json
                                                                  for judging.
