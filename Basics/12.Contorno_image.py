import cv2
import numpy as np

img = cv2.imread('Girasol.jfif')

kernel = np.ones((5, 5), np.uint8)
print(kernel)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
imgCanny = cv2.Canny(img, 300, 300)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow('Girasol', img)
cv2.imshow('Gray', imgGray)
cv2.imshow('Blur', imgBlur)
cv2.imshow('Canny', imgCanny)
cv2.imshow('Dilate', imgDialation)
cv2.imshow('Erode', imgEroded)

cv2.waitKey(0)
cv2.destroyAllWindows()
