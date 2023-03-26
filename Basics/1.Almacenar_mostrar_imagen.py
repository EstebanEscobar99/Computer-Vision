import cv2

img = cv2.imread('lion.jpg')  # leemos la imagen, el ',0' es para poner la imagen en grises
img1 = cv2.imread('lion.jpg', 0)
cv2.imshow('Lion color', img)  # (nombre que le quiero dar, imagen donde se guardo) mostrar la imagen
cv2.imshow('Lion black and white', img1)

cv2.waitKey(0)  # esperar la tecla en 0 segundos
cv2.destroyAllWindows()  # eliminar las ventanas
