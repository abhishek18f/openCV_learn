import numpy as np 
import cv2

# https://docs.opencv.org/trunk/d9/d61/tutorial_py_morphological_ops.html
# http://homepages.inf.ed.ac.uk/rbf/HIPR2/erode.htm

#STRUCTURING KERNELS
#We don't always need to make kernels manually using numpy
#OpenCV has a function, cv.getStructuringElement(). You just pass the shape and size of the kernel, you get the desired kernel. 

kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT , (5,5))
kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE , (5,5))

print(kernel1)
print(kernel2)

