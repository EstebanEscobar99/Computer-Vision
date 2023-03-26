import cv2

img = cv2.imread('huella.jpg', 0)

res = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)

# Método por umbral
_, bin1 = cv2.threshold(res, 120, 255, cv2.THRESH_BINARY_INV)

# Método Otsu
_, bin2 = cv2.threshold(res, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

cv2.imshow('Imagen umbral', bin1)
cv2.imshow('Imagen Otsu', bin2)
cv2.imshow('Imagen 1', res)

cv2.waitKey(0)
cv2.destroyAllWindows()
