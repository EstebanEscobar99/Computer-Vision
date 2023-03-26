import cv2

img1 = cv2.imread('Banano.png')
img2 = cv2.imread('Pera.png')
img3 = cv2.imread('Limon.png')
img4 = cv2.imread('Manzana.png')

Banano = cv2.resize(img1, (300, 300), interpolation=cv2.INTER_CUBIC)
Pera = cv2.resize(img2, (300, 300), interpolation=cv2.INTER_CUBIC)
Limon = cv2.resize(img3, (300, 300), interpolation=cv2.INTER_CUBIC)
Manzana = cv2.resize(img4, (300, 300), interpolation=cv2.INTER_CUBIC)

# Suma
suma_parte1 = cv2.add(Banano, Pera)  # solo sirve para dos imágenes
suma_parte2 = cv2.add(Limon, Manzana)
suma_final = cv2.add(suma_parte1, suma_parte2)

cv2.imshow('Banano', Banano)
cv2.imshow('Pera', Pera)
cv2.imshow('Limon', Limon)
cv2.imshow('Manzana', Manzana)
cv2.imshow('Frutas', suma_final)

cv2.waitKey(0)
cv2.destroyAllWindows()
