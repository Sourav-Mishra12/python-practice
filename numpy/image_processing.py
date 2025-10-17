import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image = mpimg.imread("my_image.png")
print("shape :" , image.shape)

plt.imshow(image)
plt.title("ORIGINAL PHOTO")
plt.axis("off")
plt.show()

inverted = 255 - image

plt.imshow(inverted.astype(np.uint8))
plt.title("INVERTED COLORS")
plt.axis("off")
plt.show()

if image.max() <= 1.0:
    image = (image * 255).astype(np.uint8)

blur = (image[:-1, :-1] + image[1:, :-1] + image[:-1, 1:] + image[1:, 1:]) / 4

plt.imshow(blur.astype(np.uint8))
plt.title("BLURRED")
plt.axis("off")
plt.show()