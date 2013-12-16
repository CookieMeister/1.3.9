'''image combining demonstrates PIL.Image.paste()
Unpublished work (c)2013 Project Lead The Way
Adapted from CSE Activity 1.3.7 PIL API
Version 12/16/2013 '''

import PIL
import matplotlib.pyplot as plt
import os.path              

# Open a file named image1.jpg in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))  
image1_file = os.path.join(directory, 'image1.jpg')

# Open and show the first image in a new Figure window
img1 = PIL.Image.open(image1_file)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(img1, interpolation='none')


# Open, resize, and display a second image (PNG FORMAT)
image2_file = os.path.join(directory, 'image2.png')
img2 = PIL.Image.open(image2_file)
img2_small = img2.resize((89, 87)) #eye width and height measured in plt
fig2, axes2 = plt.subplots(1, 2)
axes2[0].imshow(img2)
axes2[1].imshow(img2_small)
fig2.show()

# Paste earth into right eye and display
# Uses alpha from mask
img1.paste(img2_small, (1162, 966), mask=img2_small)
# Display
fig3, axes3 = plt.subplots(1, 2)
axes3[0].imshow(img1, interpolation='none')
axes3[1].imshow(img1, interpolation='none')
axes3[1].set_xlim(500, 1500)
axes3[1].set_ylim(1130, 850)
fig3.show()