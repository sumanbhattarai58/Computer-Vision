#edge detection of a image

import cv2

img = cv2.imread('img/car2.jpg')

img_edge = cv2.Canny(img, 140, 100)

# cv2.imshow("Image Edge", img_edge)

#use dilate to increase the edge of image
img_dil = cv2.dilate(img_edge, (1,2), iterations=1)
#use erode to decrease the edge of image
img_erode = cv2.erode(img_dil, (3,3), iterations=1)
cv2.imshow("Image Dilate", img_dil)
cv2.imshow("Image Erode", img_erode)

# cv2.imshow("Image", img)
cv2.waitKey(0)


