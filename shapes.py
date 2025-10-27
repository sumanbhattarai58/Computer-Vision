#how to draw an image

import cv2

img = cv2.imread('img/car2.jpg')
print('img shape: ', img.shape)

#draw rectangle on an image
cv2.rectangle(img, (50, 50), (100, 100), color=(148, 100, 50), thickness=-1)

#draw circle on image
cv2.circle(img, (75, 75), color=(2, 200, 50), thickness=-1, radius=10)

#draw line on an image
cv2.line(img, (0,0), (271, 192), color=(255, 0, 255),thickness=3)

#write a text on an image
cv2.putText(img, org=(10, 150), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,lineType=cv2.LINE_AA, thickness=1, color=(255, 255, 0),text="Hello car")

cv2.imshow("image", img)
 # show the image in a window named "image" (you can change it)
cv2.waitKey(0)