import cv2

img = cv2.imread('lion.jpg')

h, w, canal = img.shape  # Leer altura y ancho de la imagen

img_mitad = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)  # reducir la imagen

img_piece = img[0:int(h / 2), 0:int(w / 2)]  # cortar imagen
img_piece2 = img[int(h / 2):h, int(w / 2):w]

# cv2.imshow('Lion piece 1',img_piece)
# cv2.imshow('Lion piece 2',img_piece2)
cv2.imshow('Lion mitad', img_mitad)
cv2.imshow('Lion original', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
