import cv2

def draw (event, x, y, flags, param):
    if event==1:
        cv2.circle(img, (x,y), color=(2, 200, 50), thickness=-1, radius=10)

cv2.namedWindow("Live Drawing")
cv2.setMouseCallback("Live Drawing", draw, param=None)


img = cv2.imread('img/car1.jpg')
while True:
    cv2.imshow("Live Drawing", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

