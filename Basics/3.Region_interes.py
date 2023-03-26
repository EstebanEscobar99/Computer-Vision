import cv2

img = cv2.imread('Auto.jpg')
cv2.imshow('Auto', img)
row, column, channel = img.shape

# roi es región de interes
roi1 = img[int(row / 2):row, int(column / 2):column]
cv2.imshow('Auto recortado', roi1)

cv2.waitKey(0)
cv2.destroyAllWindows()
