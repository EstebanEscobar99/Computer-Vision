import cv2

img = cv2.imread('Animales.png', 0)

# Guardar imagen
# cv2.imwrite('Animales_gray.png',img)

cv2.imshow('Animales', img)

k = cv2.waitKey(0)

if k == 27:  # En código AISII esc es 27 (si k = esc, cierra la imagen)
    cv2.destroyAllWindows()

elif k == ord('s'):
    cv2.imwrite('imagen_guardada.png', img)
    cv2.destroyAllWindows()
