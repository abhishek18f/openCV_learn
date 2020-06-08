import numpy as np 
import cv2

img = cv2.imread('temp.jpg' , 1)
print(type(img))   #numpy array
print(img.dtype)    #unit8

#accesing a pixel value
print(img[25][54])          #returns BGR value as list

#NUmpy array methods for modifying pixel values
print(img.item(25,54,2))    #gives red value of (25,54) pixel
img.itemset((25,54,2)  , 55)    #sets that red value to 55

#Accessing image properties
print(img.shape)
print(img.size)

#Region of images a.k.a array slicing
#ROI = img[55:184 , 25:144]
#cv2.imshow('IM' , ROI)
#cv2.waitKey(0)

#splitting and merging image channels
b,g,r = cv2.split(img)
img1 = cv2.merge((b,g,r))

#cv2.imshow('blue' , b)      #only show blue matrix of the coloured image 'img
#cv2.waitKey(0)

#OR simply use numpy indexing
b1 = img[:,:,0]
#if (b1 == b).all():        b1 = b gives boolean matrix and all checks if all elements are true
#    print('yes')           #gives YES

#PADDING
#img2 = cv2.copyMakeBorder(img , 10 , 10 , 10 ,40 , cv2.BORDER_REFLECT)
#cv2.imshow('padded image' , img2)
#cv2.waitKey(0)