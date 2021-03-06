import numpy as np 
import cv2
import matplotlib.pyplot as plt 

#capture video from camera or a file
cap = cv2.VideoCapture(0)      #a video capture object 
                               #it takes argument as file name or device index[0 for default]

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')

    #arguments for VideoWriter object:
    # name of file to be saved
    #fourcc codec format
    #frames per second
    #frame resolution
out = cv2.VideoWriter('sample.mp4' , fourcc ,20 ,  (640,480))   

 
while(cap.isOpened()):        #if cap is passing the vieo OR just passs 'True'
 #Capture frame-by-frame
    ret, frame = cap.read()    #ret stores true or false from rread and frame stores image

    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))            #get gives certain prooperties of frame
        print(cap.get(4))                               #can pass name of property or number like 4 give frame height
    

        #write the frame
        out.write(frame)

        #cvtColor  (convert color)
        gray  = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)    #convert BGR to gray
        cv2.imshow('frame' , gray)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):               #keep showing each frame for 1ms
            break                                           #until q is pressed
            

cap.release()
out.release()
cv2.destroyAllWindows()        
