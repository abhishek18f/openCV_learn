import numpy as np 
import cv2
import matplotlib.pyplot as plt

#read an image
img = cv2.imread('temp.jpg', 0)   #1 for color
                                  #0 for greyscale
                                  #-1 for as such

cv2.namedWindow('image' , cv2.WINDOW_NORMAL)        
cv2.imshow('image' , img)               #window named 'image'
k = cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()             #destroys all windows
elif k == ord('s'):                     #if pressed key is s
    cv2.imwrite('saveAs_png.jpg' , img) #to save the img file after editing
    cv2.destroyAllWindows()

#printing in matplotib window
elif k == ord('m'):
    plt.imshow(img, cmap = 'gray' , interpolation = 'bicubic')      #cmap is igo=nored in 3D or higher dimension images
    plt.xticks([])                                                  #to remove xticks , empty list is passed
    plt.yticks([])
    plt.show()


#cv2.imwrite('img_gs.jpg' , img)

#Color image loaded by OpenCV is in BGR mode. 
#But Matplotlib displays in RGB mode. 
#So color images will not be displayed correctly in Matplotlib if image is read with OpenCV.