import cv2

img = cv2.imread('Auto.jpg')

cv2.imshow('Auto', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
