import numpy as np
import cv2

def get_limits(color):

    c=np.uint8([[color]])  #insert the bgr value which you watn to convert to hsv
    #print(c)
    hsvc = cv2.cvtColor(c,cv2.COLOR_BGR2HSV)  #convert it into hsv color space
    #HSV is better for color detection than BGR
    # Hue represents the actual color (0-179 in OpenCV)
    # Saturation represents color intensity
    # Value represents brightness
    # Colors are easier to isolate by hue ranges

    lowerlimit = hsvc[0][0][0] - 10,100,100 #lower limit of the range for yellow
    #hsvc[0][0][0]= Hue
    #Creates tuple: (Hue - 10, Saturation 100, Value 100)
    #The ±10 hue range catches slight color variations
    
    upperlimit = hsvc[0][0][0] + 10,255,255 #upper limit of the range for yellow
    #Creates tuple: (Hue + 10, Saturation 255, Value 255)

    #converting tuple to numpy array
    lowerlimit = np.array(lowerlimit, dtype = "uint8")
    upperlimit = np.array(upperlimit, dtype = "uint8")
    #print(lowerlimit)
    return lowerlimit,upperlimit

# blue =  (255,0,0)
# see = get_limits(blue)