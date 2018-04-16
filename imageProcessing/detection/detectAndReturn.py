#Script:  detectAndReturn.py
#Created: Thursday 04/05/18 at 05:41:28 PM
#Author:  Holden Duncan
#-----------------------------#

# A script to detect ROI's and then save the cropped
# regions. Note, the dection variables are default
# and must be changed within the script, but the target
# image and save destination may be specified on command line.

# Use: python detectAndReturn.py <imageName.jpg> <path/to/save/desitination>


import sys
from sluavImage import *

fault = False

#print( sys.argv[1] + ' ' +sys.argv[2])

if(len(sys.argv) != 3):
    fault = True
    raise IOError('Must include the path to the image and a destination for the image output')

try:
    img = sluavImage(sys.argv[1])
except:
    raise IOError('The image does not exist or the path is bad')
    fault = True

raw_name = sys.argv[1]
filename = ''

for i in range(len(raw_name)-1,0,-1):
    if raw_name[i] == '/':
        break
    else:
        filename = raw_name[i] + filename

filename = filename[:(filename.rfind("."))]


if not fault:
    img.getROIs(550, 100, )
    img.removeDups(50)


    for i in range(len(img)):
        cv2.imwrite(sys.argv[2] + filename + '_ROI_' + str(i) + '.jpeg', img.getRegion(i))

    img.drawROIs()
    cv2.imwrite(sys.argv[2]+'BOX_'+filename+ '.jpeg', img._img)
