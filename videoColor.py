import cv2
import numpy as np

def separate_channels(image):
    # Split the image into individual channels
    b, g, r = cv2.split(image)

    # Create an empty image with zeros
    zeros = np.zeros_like(b)

    # Create separate images for each channel
    blue_channel = cv2.merge([b, zeros, zeros])
    green_channel = cv2.merge([zeros, g, zeros])
    red_channel = cv2.merge([zeros, zeros, r])

    return blue_channel, green_channel, red_channel

# Open a connection to the primary webcam
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        break

    # Separate the channels
    blue, green, red = separate_channels(frame)

    # Merge the channels back into a color image
    color_image = cv2.merge([blue[:, :, 0], green[:, :, 1], red[:, :, 2]])

    # Stack images horizontally
    top_row = np.hstack((color_image, red))
    bottom_row = np.hstack((green, blue))

    # Stack rows vertically
    combined_image = np.vstack((top_row, bottom_row))

    # Display the result
    cv2.imshow("Combined Images", combined_image)

    # Check for key press, break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
