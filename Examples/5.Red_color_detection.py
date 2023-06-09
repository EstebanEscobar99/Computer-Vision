import cv2
import numpy as np

captura = cv2.VideoCapture(0)

redBajo1 = np.array([0, 100, 20], np.uint8)
redAlto1 = np.array([0, 255, 255], np.uint8)

redBajo2 = np.array([175, 100, 20], np.uint8)
redAlto2 = np.array([179, 255, 255], np.uint8)

while True:
    ret, frame = captura.read()

    if ret:
        frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        maskRed1 = cv2.inRange(frameHSV, redBajo1, redAlto1)
        maskRed2 = cv2.inRange(frameHSV, redBajo2, redAlto2)
        maskRed = cv2.add(maskRed1, maskRed2)  # El color lo detecta y lo muestra en blanco
        maskRedvis = cv2.bitwise_and(frame, frame, mask=maskRed)  # El color se muestra según lo que detecta

        cv2.imshow('maskRedvis', maskRedvis)
        cv2.imshow('maskRed', maskRed)
        cv2.imshow('video', frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

captura.release()
cv2.destroyAllWindows()
