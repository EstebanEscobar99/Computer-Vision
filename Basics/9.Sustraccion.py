import cv2

img1 = cv2.imread('Krilin.png')
img2 = cv2.imread('Goku.png')

Krilin = cv2.resize(img1, (300, 300), interpolation=cv2.INTER_CUBIC)
Goku = cv2.resize(img2, (300, 300), interpolation=cv2.INTER_CUBIC)

# Restar
resta1 = cv2.subtract(Krilin, Goku)
resta2 = cv2.subtract(Goku, Krilin)

# Suma
suma = cv2.add(resta1, resta2)

cv2.imshow('Krilin', Krilin)
cv2.imshow('Goku', Goku)
cv2.imshow('Detecta Goku', resta1)
cv2.imshow('Detecta Krilin', resta2)
cv2.imshow('Both', suma)

cv2.waitKey(5000)
cv2.destroyAllWindows()
