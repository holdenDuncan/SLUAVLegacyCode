import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('test2.jpg', 0)
img = cv2.imread('test2.jpg', 0)
img2 = cv2.imread('test2.jpg', 0)
img3 = cv2.imread('test2.jpg', 0)
img4 = cv2.imread('test2.jpg', 0)
img5 = cv2.imread('test2.jpg', 0)
img6 = cv2.imread('test2.jpg', 0)

mask = np.zeros(img1.shape, dtype = "uint8")

shape = "Unknown"
#*************** start my contour bullshit ********************** http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contours_begin/py_contours_begin.html
gray = cv2.medianBlur(img, 3)
gray = cv2.threshold(gray, 0, 255,
        cv2.THRESH_TOZERO | cv2.THRESH_OTSU) [1]
#meadian bluring and thresholding 

edges = cv2.Canny(gray, 100, 200)

plt.subplot(121),plt.imshow(edges,cmap = 'gray')
plt.title('Edges'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(gray,cmap = 'gray')
plt.title('Thresh'), plt.xticks([]), plt.yticks([])
plt.show()

image, contours, hierarchy = cv2.findContours(gray,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
#image, contours, hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
# cv2.RETR_TREE = contour retrieval mode; cv2.CHAIN_APPROX_SIMPLE = contour approximation method; contours = list of all contours in image w each contour a numpy array of (x,y) coordinates of boundary points of the object

#the following draws contours bigger than 400 pixels
scontours = []
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 300 : #300 is subject to change when we use actual images
        scontours.append(contour)
cimg = cv2.drawContours(mask, scontours, -1, (255,255,255), 1)
# -1 indicates to draw all contours; last argument of drawContours is thickness

plt.subplot(121),plt.imshow(img1, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(cimg, cmap = 'gray')
plt.title('Contour of Edges'), plt.xticks([]), plt.yticks([])
plt.show()
#**************** end my contour bullshit ***************************************


#%%%%%%%%%%%%%%%% start my urge to purge merge %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
numberofpoints = 0
for contour in scontours:
  for point in contour:
    numberofpoints = numberofpoints +1

allcountours = np.zeros((numberofpoints,1,2), dtype=np.int32)
count = 0
for contour in scontours:
    for point in contour:
      allcountours[count][0] = [point[0][0],point[0][1]]
      count = count + 1
cnt = allcountours
#%%%%%%%%%%%%%%%%% end my urge to purge merge %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


#----------- start my shippity shape shit---------------------------------
#https://docs.opencv.org/3.1.0/dd/d49/tutorial_py_contour_features.html
#https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_contours/py_contours_more_functions/py_contours_more_functions.html#contours-more-functions

k = cv2.isContourConvex(cnt)
print("K: ", k)

perimeter = cv2.arcLength(cnt, True)
epsilon = 0.1*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt, epsilon, True)
print("Perimeter", perimeter)
print("Approx", approx)
if k:
	#figure out if star or plus sign
	if len(approx) == 10:
		shape = "Star"
	elif len(approx) == 12:
		shape = "Plus"
else:
	if len(approx) == 3:
		shape = "Triangle"
	elif len(approx) == 4:
		(x, y, w, h) = cv2.boundingRect(approx)
		ar = w / float(h)
		shape = "Square" if ar >= 0.95 and ar <=1.05 else "Rectangle"
	elif len(approx) == 5:
		shape = "Pentagon"

print(shape)










