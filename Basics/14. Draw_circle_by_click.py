import cv2
import matplotlib.pyplot as plt


def display(image, cmap=None):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111)
    ax.imshow(image, cmap=cmap)


img1 = cv2.imread('Guatape.jfif')
img = cv2.resize(img1, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
display(img)


# Step 1. Define callback function
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, center=(x, y), radius=5,
                   color=(87, 184, 237), thickness=-1)

    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, center=(x, y), radius=10,
                   color=(87, 184, 237), thickness=1)


# Step 2. Call the window
img1 = cv2.imread('Guatape.jfif')
img = cv2.resize(img1, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing', draw_circle)

# Step 3. Execution 
while True:
    cv2.imshow('my_drawing', img)
    if cv2.waitKey(10) & 0xFF == 27:
        break

cv2.destroyAllWindows()
