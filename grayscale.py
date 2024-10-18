import imageio as img
import numpy as np
import matplotlib.pyplot as plt

path = "C:\\SMT_5\\Pengolahan_Citra\\download2.jpg"

image = img.imread(path)

# Convert the RGB image to grayscale using the formula:
# grayscale_value = 0.2989 * R + 0.5870 * G + 0.1140 * B
grayscale_image = np.dot(image[...,:3], [0.2989, 0.5870, 0.1140])

# Calculate histogram (values between 0 and 255)
histogram, bin_edges = np.histogram(grayscale_image, bins=256, range=(0, 255))

# Plot histogram
plt.figure(figsize=(10, 6))
plt.plot(bin_edges[0:-1], histogram, color='black')
plt.title("Histogram of Grayscale Image")
plt.xlabel("Pixel Intensity (0-255)")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
