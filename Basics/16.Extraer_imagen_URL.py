import urllib.request
import cv2

urllib.request.urlretrieve('https://www.gettyimages.es/gi-resources/images/500px/983794168.jpg', 'file_name')

img = cv2.imread('file_name')
cv2.imshow('i', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
