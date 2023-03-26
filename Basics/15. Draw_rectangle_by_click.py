import cv2

# Step 1. Define callback function
drawing = False
ix = -1
iy = -1


def draw_rectangle(event, x, y, flags, params):
    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.rectangle(img, pt1=(ix, iy), pt2=(x, y),
                          color=(94, 196, 224), thickness=-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, pt1=(ix, iy), pt2=(x, y),
                      color=(94, 196, 224), thickness=-1)


# Step 2. Call the window
img1 = cv2.imread('Guatape.jfif')
img = cv2.resize(img1, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing', draw_rectangle)

# Step 3. Execution
while True:

    cv2.imshow('my_drawing', img)
    if cv2.waitKey(10) & 0xFF == 27:
        break

cv2.destroyAllWindows()
