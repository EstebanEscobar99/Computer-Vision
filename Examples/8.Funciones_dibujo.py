import cv2
import numpy as np

imagen = 255 * np.ones((400, 600, 3), dtype=np.uint8)

# Dibujar línea
cv2.line(imagen, (0, 0), (600, 400), (255, 0, 0), 4)

# Dibujar rectángulo
cv2.rectangle(imagen, (50, 80), (200, 200), (0, 255, 0), 1)

# Dibujar circulo
cv2.circle(imagen, (300, 200), 100, (255, 255, 0), -1)  # En el grosor (último argumento) el -1 indica relleno

# Visualizar texto
# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(imagen,'Practicando con OpenCV',(10,30),font,1,(0,255,255),2,cv2.LINE_AA)

cv2.putText(imagen, 'Practicando con OpenCV', (10, 30), 0, 1, (0, 255, 255), 2, cv2.LINE_AA)
cv2.putText(imagen, 'Practicando con OpenCV', (10, 60), 1, 1, (0, 255, 255), 2, cv2.LINE_AA)
cv2.putText(imagen, 'Practicando con OpenCV', (10, 90), 2, 1, (0, 255, 255), 2, cv2.LINE_AA)
cv2.putText(imagen, 'Practicando con OpenCV', (10, 120), 3, 1, (0, 255, 255), 2, cv2.LINE_AA)
cv2.putText(imagen, 'Practicando con OpenCV', (10, 150), 4, 1, (0, 255, 255), 2, cv2.LINE_AA)
cv2.putText(imagen, 'Practicando con OpenCV', (10, 180), 5, 1, (0, 255, 255), 2, cv2.LINE_AA)
cv2.putText(imagen, 'Practicando con OpenCV', (10, 210), 6, 1, (0, 255, 255), 2, cv2.LINE_AA)
cv2.putText(imagen, 'Practicando con OpenCV', (10, 240), 7, 1, (0, 255, 255), 2, cv2.LINE_AA)

cv2.imshow('Imagen', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
