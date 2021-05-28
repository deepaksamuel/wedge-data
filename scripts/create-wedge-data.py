#%%
#Import all libraries we will use
import random
import numpy as np
import cv2
import matplotlib.pyplot as plt

#let's create a 6 x 6 matrix with all pixels in black color
# img = np.zeros((6,6,3),np.uint8)

# #let's use "for" cycle to change colorspace of pixel in a random way
# for x in range(6):
#     for y in range(6):
#         #We use "0" for black color (do nothing) and "1" for white color (change pixel value to [255,255,255])
#         value = random.randint(0,1)
#         if value == 1:
#             img[x,y] = [150,150,150]

# #save our image as a "png" image
# cv2.imwrite("6_x_6.png",img)
#im2 = cv2.imread("../wedge-data-1000000-2cm/img/0.1-TW=0.1-BW

im2 = cv2.imread("../wedge-data-1000000-2cm/img/0.1-TW-20.0-BW.txt.png",cv2.IMREAD_UNCHANGED)
#plt.imread("../wedge-data-1000000-2cm/img/0.1-TW-0.1-BW.txt.png")
# cv2.namedWindow( "Display window")
# cv2.imshow( "Display window", im2 ); 
plt.imshow(im2)
plt.show()
# %%
