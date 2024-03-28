import cv2
import matplotlib.pyplot as plt

img_path = "cv_ws/image/cat.jpg"

img = plt.imread(img_path)
fig, axs = plt.subplots(2,2,figsize=(10,10))
axs[0,0].imshow(img)
axs[0,1].imshow(img[:,:,0], cmap='Reds')
axs[1,0].imshow(img[:,:,1], cmap='Greens')
axs[1,1].imshow(img[:,:,2], cmap='Blues')
axs[0,0].axis('off')
axs[0,1].axis('off')
axs[1,0].axis('off')
axs[1,1].axis('off')
plt.show()


cv2.waitKey(0) 
cv2.destroyAllWindows() 