# Ejercicio
"""Crear un programa que genere la imagen del conejo a tamaño triplicado y en escala de grises"""

import cv2

# Leer imagen
# img = cv2.imread('Animales.png') # Zorro RGB
img2 = cv2.imread('Animales.png', 0)  # Zorro escala de grises

# Región de interés
h, w = img2.shape
roi = img2[int(h / 3.2):int(1.55 * h / 3), int(3 * w / 4):w]

# Escalar imagen
res = cv2.resize(roi, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)

# Mostrar imagen
# cv2.imshow('Animales',img)
cv2.imshow('Animales en escala de grises', img2)
cv2.imshow('Conejo', roi)
cv2.imshow('Conejo grande', res)

cv2.waitKey(0)
cv2.destroyAllWindows()
