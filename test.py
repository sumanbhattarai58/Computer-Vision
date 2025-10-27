import cv2
import numpy as np 

#Read an image
img=cv2.imread('img/car1.jpg',0)
print(img)
print(type(img))
print(img.shape)

#write image


#Convert to grayscale
# gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# print(gray.shape)

#remove red color from the image
# img[:,:,2]=0

#see an individual color effect
# imgBlue = img[:,:,0]
# imgGreen = img[:,:,1]
# imgRed = img[:,:,2]

# newimg = np.hstack((imgBlue, imgGreen, imgRed))

#resize an image
# resize_image = cv2.resize(img,(256,256))



# #Display the image
# cv2.imshow('image',resize_image)
# print(resize_image.shape)
# cv2.waitKey(0)

