import cv2

img = cv2.imread('img/car1.jpg')

# Blurring the image using a Gaussian kernel
k_size = 9
blur_image = cv2.blur(img, (k_size, k_size))

#blur only the part of image
img[100:400, 150:350] = cv2.blur(img[100:400, 150:350], (k_size, k_size))
cv2.imshow("Image", img)
cv2.waitKey(0)


