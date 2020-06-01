import numpy as np 
import cv2

#read an image
img = cv2.imread('temp.jpg', 0)   #1 for color
                                  #0 for greyscale
                                  #-1 for as such

cv.imshow('image' , img)

