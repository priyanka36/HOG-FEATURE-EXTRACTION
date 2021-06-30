# hog using skimage library python

from skimage.io import imread
from skimage.feature import hog
import matplotlib.pyplot as plt 

tesla_image = imread("tesla.jpg")
_, hog_image = hog(tesla_image, orientations=8, pixels_per_cell=(16, 16),
cells_per_block=(1, 1), visualize=True, multichannel=True)
plt.imshow(hog_image)
plt.show()

# The hog() method accepts 6 arguments.

# image:Represent the image on which we want to perform the hog extraction.

# orientations:Define the number of bins in the histogram.

# pixels_per_cell: Define the number of grids for per patch.

# cells_per_block:It defines the number of cells for every block.

# visualize:A boolean value that specifies whether to return the Image of HOG.

# multichannel:A boolean value True sets the last dimension to the color channel rather than spatial.

