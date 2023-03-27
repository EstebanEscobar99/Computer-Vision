import cv2
import numpy as np
import imutils

image = cv2.imread('Sacapuntas.jpg', 0)
image = imutils.resize(image, width=400)  # Se puede omitir esta línea

_, binarizada = cv2.threshold(image, 210, 255, cv2.THRESH_BINARY)
_, binarizadaInv = cv2.threshold(image, 210, 255, cv2.THRESH_BINARY_INV)

cv2.imshow('Tipos: Binary - Binary Inv', np.hstack([binarizada, binarizadaInv]))
cv2.waitKey(0)
cv2.destroyAllWindows()
