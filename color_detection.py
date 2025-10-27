import cv2
import numpy as np
from PIL import Image

from color1 import get_limits

#yellow color in BGR color space
yellow =  (0 ,255,255)

cap = cv2.VideoCapture(0)   #0 refers to default camera
while True:
    ret, frame = cap.read()

    
# BGR to HSV color space
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #Converts the camera frame from BGR to HSV color space for better color detection.
    
    lower_limit, upper_limit = get_limits(yellow)
  
    mask = cv2.inRange(hsvImage, lower_limit, upper_limit)
    #Creates a binary mask where pixels within the color range are white (255), others are black (0)
    #Isolates only the yellow-colored regions in the image

    mask_ = Image.fromarray(mask)
    #Converts the NumPy array mask to a PIL Image object.

    bbox = mask_.getbbox()
    #Returns the bounding box of non-zero regions as (left, top, right, bottom)
    if bbox is not None:
        x1, y1 , x2, y2 = bbox
    #x1, y1: Top-left corner
    #x2, y2: Bottom-right corner (not width/height - common misunderstanding)
# Draw a rectangle around the detected object
    frame= cv2.rectangle(frame,(x1,y1),(x2,y2),yellow, 3)
#     Draws a yellow rectangle on the original frame
# (x1, y1): Start point (top-left)
# (x2, y2): End point (bottom-right)
# yellow: Color of the rectangle
# 3: Thickness in pixels

    cv2.imshow('original', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #Allows user to exit by pressing 'q'
cap.release()
cv2.destroyAllWindows()