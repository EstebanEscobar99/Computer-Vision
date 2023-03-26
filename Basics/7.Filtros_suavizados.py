import cv2
import numpy as np

# Leer la imagen
img = cv2.imread('lion.jpg')

# Filtro promedio: reemplaza cada pixel en la imagen con el valor promedio del vecindario
f1 = cv2.blur(img, (3, 3))

# Filtro Gaussiano: Especifica el ancho y alto del kernel, que debe ser positivo e impar. 
# También especifica la desviación estándar en las direcciones X e Y. 
# Si solo se especifica sigmaX, sigmaY se toma como igual a sigmaX. 
# Si ambos se dan como ceros, se calculan a partir del tamaño del kernel.
f2 = cv2.GaussianBlur(img, (5, 5), 0)

# Filtro mediano: Calcula la mediana de todos los píxeles debajo de la ventana del kernel y el píxel central se
# reemplaza con este valor.
f3 = cv2.medianBlur(img, 5)

# Filtro convolución 2D
# Crear un kernel
filtro4 = np.ones((5, 5), np.float32) / 25
# Filtra la imagen utilizando el kernel anterior
f4 = cv2.filter2D(img, -1, filtro4)

# Mostrar la imagen
cv2.imshow('Lion', img)
cv2.imshow('Lion filtro promedio', f1)
cv2.imshow('Lion filtro Gaussiano', f2)
cv2.imshow('Lion filtro mediano', f3)
cv2.imshow('Lion filtro convolución', f4)

cv2.waitKey(0)
cv2.destroyAllWindows()
