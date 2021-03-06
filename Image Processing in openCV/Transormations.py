import numpy as np 
import cv2

#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_geometric_transformations/py_geometric_transformations.html


#OpenCV provides two transformation functions, cv2.warpAffine and cv2.warpPerspective, with which you can have all kinds of transformations. 
#cv2.warpAffine takes a 2x3 transformation matrix 
#while cv2.warpPerspective takes a 3x3 transformation matrix as input

#SCALING
# Different interpolation methods are used.
# Preferable interpolation methods are cv2.INTER_AREA for shrinking and cv2.INTER_CUBIC (slow) & cv2.INTER_LINEAR for zooming
#Either fx , fy that are scaling factors(in this case 0.5 , 0.5) needs to be mentioned 
#Or dest frame and size needs to be mentioned(in this case none) 
img  = cv2.imread('temp.jpg')
img1 = cv2.resize(img, None , None , 0.5 , 0.5 ,  cv2.INTER_AREA  )         #shrink height and width by 0.5
cv2.imshow('img' ,img)
# cv2.imshow('img1' , img1)
# cv2.waitKey(0)

#TRANSLATION
#   The function warpAffine transforms the source image using the specified matrix:
#   dst(x,y)=src(M11x+M12y+M13,M21x+M22y+M23)
rows, cols , _ = img.shape
M = np.array([[1 , 0 , 80 ] , [0, 1 , 40]] , np.float32)    #Transformation matrix for shift of 80px in x and that of 40px in y
                                                            #declare array in float32 dtype
#Third argument of the cv2.warpAffine() function is the size of the output image, 
#which should be in the form of (width, height). Remember width = number of columns, and height = number of rows.
img2 = cv2.warpAffine(img , M , (cols , rows))
# cv2.imshow('img2' , img2)
# cv2.waitKey(0)

#ROTATION
#to get rotation matrix we use getRotationMatrix2D function
#retval	=	cv.getRotationMatrix2D(	center, angle, scale	)
rotM = cv2.getRotationMatrix2D((cols/3 , 2*rows/3) , 45 , 1)
img3 = cv2.warpAffine(img , rotM, (cols , rows))
# print(rotM)
# [[   0.70710678    0.70710678 -403.67532368]
#  [  -0.70710678    0.70710678  465.44155877]]
cv2.imshow('img3' , img3)
cv2.waitKey(0)

#PERSPECTIVE TRANSFORMATION
#For perspective transformation, you need a 3x3 transformation matrix. 
#Straight lines will remain straight even after the transformation. 
#To find this transformation matrix, you need 4 points on the input image and corresponding points on the output image.
# Among these 4 points, 3 of them should not be collinear. 
#Then the transformation matrix can be found by the function cv.getPerspectiveTransform. 
#Then apply cv.warpPerspective with this 3x3 transformation matrix.

