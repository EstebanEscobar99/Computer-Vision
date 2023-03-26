import cv2

img = cv2.imread('lion.jpg')  # Imagen RGB
img2 = cv2.imread('lion.jpg', 0)  # Imagen escala de grises
img3 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Conversión BGR - Grises

cv2.imshow('Lion', img)
row, column, channel = img.shape

# roi es región de interés
roi1 = img[int(row / 2):row, int(column / 2):column]
# cv2.imshow('Lion grises',img3)

# Escalar
res = cv2.resize(img, None, fx=0.75, fy=0.75, interpolation=cv2.INTER_CUBIC)
res2 = cv2.resize(img, (200, 200), interpolation=cv2.INTER_CUBIC)
cv2.imshow('Lion resize', res)
cv2.imshow('Lion resize 2', res2)

cv2.waitKey(0)
cv2.destroyAllWindows()
