import cv2

captura = cv2.VideoCapture(0)  # webcam, 0 o 1 para seleccionar camara
# captura = cv2.VideoCapture('Video salida.avi') # leer un video
salida = cv2.VideoWriter('Video salida.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640, 480))

while captura.isOpened():  # while True: también se puede usar
    ret, imagen = captura.read()

    if ret:
        cv2.imshow('video', imagen)
        salida.write(imagen)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    else:
        break

captura.release()
salida.release()
cv2.destroyAllWindows()
