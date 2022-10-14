from hashlib import new
import cv2
import numpy as np
import matplotlib.pyplot as plt

# read in image and resize
img = cv2.imread('chessboard1.jpg')

# percent by which the image is resized
scale_percent = 50

# calculate the 50 percent of original dimensions
new_width = int(img.shape[1] * scale_percent / 100)
new_height = int(img.shape[0] * scale_percent / 100)

# dsize
dsize = (new_width, new_height)

# resize image
img = cv2.resize(img, dsize)

# show resized image
cv2.imshow('resized', img)

# corner coordinates (will get from outermost coordinates of mask r-cnn board segmentation)
# coordinates are taken clockwise starting in top left corner of board
# for now it is hardcoded
coords = np.float32([[405,231], [2173,223], [2545,1571], [55,1655]]) * scale_percent / 100

# get resized image height and width
new_height, new_width, _ = img.shape

# new corner coordinates will stretch to fit image window
new_coords = np.float32([[0,0], [new_width, 0], [new_width, new_height], [0, new_height]])

# use coordinates to compute perspective transform matrix
ptm = cv2.getPerspectiveTransform(coords, new_coords)

# use perspective transform matrix to transform resized image
trans_img = cv2.warpPerspective(img, ptm, (new_width, new_height))

# show transformed image
cv2.imshow('perspective transformed image', trans_img)

# hold image windows open indefinitely
cv2.waitKey(0)

# close all windows when done
cv2.destroyAllWindows()