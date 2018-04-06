import cv2
import numpy as np

class sluavImage(object):

    def __init__(self, imgFile):
        """ The object is initilized with a string that is the path to the intended
photo for manipulation. Function library is currently not robust and will not throw applicable errors."""
        self._img = cv2.imread(imgFile)
        if(self._img is None):
            raise IOError('File failed to initialize the object. Is the path correct?')
        self._ROIs = []
        self._path = imgFile

    def __getitem__(self, index):
        """Retrieves the (xMax, yMax, xMin, yMin) of a ROI at the given index"""
        return self._ROIs[index]

    def __str__(self):
        """A friendly to read and informative str repersentation of the object"""
        output = 'Image at: ' + self._path + ' with ' + str(len(self._ROIs)) + ' number of regions.'
        return output

    def __repr__(self):
        output = 'Obeject id of: ' + str(id(self)) + " based on " + self._path + " with " + str(len(self._ROIs)) + ' number of regions'
        return output
 
    def __len__(self):
    	"""The length is the number of ROIs"""
    	return(len(self._ROIs))
    	
    def resize(self, SCALING = 1.0):
        """A function for resizing the img of an object"""
        newImg = cv2.resize(self._img,None,fx=SCALING, fy=SCALING, interpolation = cv2.INTER_LINEAR)
        self._img = newImg
        #return newImg
        
    def removeDups(self, margin = 10):
        """A function to remove duplicate ROIs by grouping ROIs based on
the given margin and averaging out the values to create the best single
region."""
        ## Storing the locations of duplicates as a list with entries of lists with intergers
        ## indicating the idex of dups. 
        dupLocs = []
        counter = -1
        done = False

        while not done:

            counter += 1
            xMax, yMax, xMin, yMin = self._ROIs[counter]
            dupSet = []
            innerCounter = -1
            
            for xMaxCheck, yMaxCheck, xMinCheck, yMinCheck in self._ROIs:
                innerCounter += 1
                if xMaxCheck - margin < xMax < xMaxCheck + margin:
                    dupSet.append(innerCounter)

            dupLocs.append(dupSet)

            if counter == len(self._ROIs) - 1:
                done = True

        ## Using dupLocs to create a new list of ROIs where the dups have been
        ## averaged into a single bigger ROI
        newROIs = []
        prevLocs = []
        avgXMax = 0
        avgYMax = 0
        avgXMin = 0
        avgYMin = 0
        for locs in dupLocs:
            counter = 0
            avgXMax = float(0)
            avgYMax = float(0)
            avgXMin = float(0)
            avgYMin = float(0)
            
            if locs != prevLocs: # Prevents the duplicate lists from running.
                for entries in locs: # Takes the locs of the Dups and adds all the components
                    counter += 1
                    xMax, yMax, xMin, yMin = self._ROIs[entries]
                    avgXMax += xMax
                    avgYMax += yMax
                    avgXMin += xMin
                    avgYMin += yMin

                avgXMax /= counter # Uses the counter and divides by the number of entries
                avgYMax /= counter # to produce the average
                avgXMin /= counter
                avgYMin /= counter

                newROIs.append( (int(avgXMax), int(avgYMax), int(avgXMin), int(avgYMin)) )
                
            prevLocs = locs

        self._ROIs = newROIs
        #return newROIs
        
        
    def getROIs(self, UPPER_TOLERANCE = 100, LOWER_TOLERANCE= 35, BUFFER = 10):
        """ Assigns the sluavImage object Regions Of Interest, i.e.
possible targets"""
        
        try:
            img = cv2.cvtColor(self._img, cv2.COLOR_BGR2GRAY)
        except:
            img = self._img

        try:
            height,width = img.shape
        except ValueError:
            height, width, color = img.shape

        vis = img.copy()
        mser = cv2.MSER_create()

        regions = mser.detectRegions(img)
        hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions[0]]

        ROIs = []
        for i in range(len(hulls)):
            rectMax = hulls[i].max(axis=0)
            rectMin = hulls[i].min(axis=0)

            xMax = rectMax.item(0) + BUFFER
            xMin = rectMin.item(0) - BUFFER
            yMax = rectMax.item(1) + BUFFER
            yMin = rectMin.item(1) - BUFFER

            if xMax - xMin > UPPER_TOLERANCE or yMax - yMin > UPPER_TOLERANCE:
                pass
            elif xMax - xMin < LOWER_TOLERANCE or yMax - yMin < LOWER_TOLERANCE:
                pass
            elif xMax > width or xMin < 0 or yMax > height or yMin < 0:
                pass
            else:
                ROIs.append((xMax,yMax,xMin,yMin))

        self._ROIs = ROIs

    def getRegion(self, index):
        """Returns an opencv image of the indexed region.
Useful for saving/exporting the region."""
        xMax, yMax, xMin, yMin = self._ROIs[index]
        section = self._img[yMin:yMax, xMin:xMax]
        return section

    def drawROIs(self, color = (0,0,255)):
        """Draws frames on the image for visualization of the detected
regions. Draws red by default but may by specified by a BGR tuple input.
show must be called after drawROIs to actually display.
Note: This function does change the original image and is currently
irreversable."""
        counter = 0
        for xMax, yMax, xMin, yMin in self._ROIs:
            counter += 1
            #cv2.putText(img, str(counter),(xMax,yMax), font, 1,(0,0,255),2)
            cv2.line(self._img,(xMin,yMin),(xMax,yMin),color,1)
            cv2.line(self._img,(xMax,yMin),(xMax,yMax),color,1)
            cv2.line(self._img,(xMax,yMax),(xMin,yMax),color,1)
            cv2.line(self._img,(xMin,yMax),(xMin,yMin),color,1)
        return

    def show(self):
        """Displays the current img of the object. Press Esc key to exit
the window."""
        cv2.imshow('image', self._img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    
        
