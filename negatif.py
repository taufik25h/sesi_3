import imageio as img
import numpy as np
import matplotlib.pyplot as plt

path = "C:\\SMT_5\\Pengolahan_Citra\\download2.jpg"

imgNegatif = img.imread(path)
redNegatif = imgNegatif[:,:,0]
rN_hist, bins = np.histogram(redNegatif,bins=256,range=[0,256])

imgPositif = 255 - imgNegatif
redPositif = imgPositif[:,:,0]
rP_hist, bins = np.histogram(redPositif,bins=256,range=[0,256])

plt.figure(figsize=(10,10))

plt.subplot(2,2,1)
plt.imshow(imgNegatif)

plt.subplot(2,2,2)
plt.imshow(imgPositif)

plt.subplot(2,2,3)
plt.plot(rN_hist, color='red')

plt.subplot(2,2,4)
plt.plot(rP_hist, color='blue')

plt.tight_layout()
plt.show()