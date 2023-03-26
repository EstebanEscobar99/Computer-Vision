import cv2

img1 = cv2.imread('Torre_Eiffel.jpg')

# Redimensionamiento
res = cv2.resize(img1, (560, 560), interpolation=cv2.INTER_CUBIC)

# Giro del dron
rows, cols, channel = res.shape

M = cv2.getRotationMatrix2D((cols / 2, rows / 2), -60, 1)  # (centro de rotación, ángulo, escala)

dst = cv2.warpAffine(res, M, (cols, rows),
                     0)  # (imagen de entrada, matriz de transformación, tamaño de la imagen, método de interpolación)

cv2.imshow('Imagen dron', img1)
cv2.imshow('Imagen reescalada', res)
cv2.imshow('Imagen final', dst)
cv2.imwrite('dron.jpg', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
