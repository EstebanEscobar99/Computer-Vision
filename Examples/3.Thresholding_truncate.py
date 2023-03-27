import cv2
import imutils

image = cv2.imread('Sacapuntas.jpg', 0)
image = imutils.resize(image, width=400)  # Se puede omitir esta línea

_, Trunc = cv2.threshold(image, 210, 255, cv2.THRESH_TRUNC)  # Si es mayor a 210, toma el valor de 210

cv2.imshow('Tipos: Trunc', Trunc)
cv2.waitKey(0)
cv2.destroyAllWindows()
