import cv2
import numpy as np

def separate_channels(image):
    b, g, r = cv2.split(image)

    zeros = np.zeros_like(b)

    blue_channel = cv2.merge([b, zeros, zeros])
    green_channel = cv2.merge([zeros, g, zeros])
    red_channel = cv2.merge([zeros, zeros, r])

    return blue_channel, green_channel, red_channel

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    blue, green, red = separate_channels(frame)

    color_image = cv2.merge([blue[:, :, 0], green[:, :, 1], red[:, :, 2]])

    top_row = np.hstack((color_image, red))
    bottom_row = np.hstack((green, blue))

    combined_image = np.vstack((top_row, bottom_row))

    cv2.imshow("Combined Images", combined_image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
