from ExactHistogramSpecification import ExactHistogramMatcher # This package
from PIL import Image # or use your preferred way of reading image data
import numpy as np # numerical stack
import matplotlib.pylab as plt # plotting
import seaborn as sns # fancier plotting

# Load images
reference_image = np.array(Image.open('image_a.png'))
change_image = np.array(Image.open('image_b.png'))

# Get histogram
reference_histogram = ExactHistogramMatcher.get_histogram(reference_image)
# Match image to histogram
new_image = np.round(ExactHistogramMatcher.match_image_to_histogram(change_image, reference_histogram)).astype(np.uint8)

# For validation:
# Histogram of original image
change_histogram = ExactHistogramMatcher.get_histogram(change_image)
# Histogram of newly created image
new_histogram = ExactHistogramMatcher.get_histogram(reference_image)

# Plotting: Evaluate histogram match
sns.set_style('whitegrid')
fig, ax = plt.subplots(3,2, figsize=(10,8))

# Input Image
ax[0,0].set_title('Input Image')
ax[0,0].imshow(change_image)
ax[0,0].axis('off')

ax[0,1].plot(range(256),change_histogram[:,0].T,color='r', alpha=.4)
ax[0,1].plot(range(256),change_histogram[:,1].T,color='g', alpha=.4)
ax[0,1].plot(range(256),change_histogram[:,2].T,color='b', alpha=.4)
ax[0,1].set_xlim([0,255])

# Reference Image
ax[1,0].set_title('Reference Image')
ax[1,0].imshow(reference_image)
ax[1,0].axis('off')

ax[1,1].plot(range(256),reference_histogram[:,0].T,color='r', alpha=.4)
ax[1,1].plot(range(256),reference_histogram[:,1].T,color='g', alpha=.4)
ax[1,1].plot(range(256),reference_histogram[:,2].T,color='b', alpha=.4)
ax[1,1].set_xlim([0,255])

# New Image
ax[2,0].set_title('New Image')
ax[2,0].imshow(new_image)
ax[2,0].axis('off')

ax[2,1].plot(range(256),new_histogram[:,0].T,color='r', alpha=.4)
ax[2,1].plot(range(256),new_histogram[:,1].T,color='g', alpha=.4)
ax[2,1].plot(range(256),new_histogram[:,2].T,color='b', alpha=.4)
ax[2,1].set_xlim([0,255])

# Saving
plt.tight_layout()
fig.savefig('validate.png',bbox_inches='tight')
