import cv2
img = cv2.imread('img/car1.jpg')

img1=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_crop = img[100:300, 100:400]
cv2.imwrite('cropped_image.jpg',img_crop)

# cv2.imshow('image', img1)
# cv2.imshow('image', img2)
cv2.imshow('image', img_crop)
cv2.waitKey(0)

