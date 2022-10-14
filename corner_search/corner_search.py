import numpy as np
import sys

# sample mask r-cnn segmentation np array
sample_mask = np.float32([[0, 0, 0, 0, 0, 0, 0, 0,],
                          [0, 0, 0, 0, 0, 0, 0, 0,],
                          [0, 0, 1, 0, 0, 0, 0, 0,],
                          [0, 0, 1, 1, 1, 1, 1, 0,],
                          [0, 0, 1, 1, 1, 1, 0, 0,],
                          [0, 0, 1, 1, 1, 1, 0, 0,],
                          [0, 0, 1, 1, 1, 1, 0, 0,],
                          [0, 0, 0, 0, 0, 1, 0, 0,],      
                          [0, 0, 0 ,0 ,0 ,0 ,0 ,0]])

# top left, top right, bottom left, and bottom right corners [width, height]
tl = np.float32([sys.maxint, sys.maxint])
tr = np.float32([-sys.maxint - 1, sys.maxint])
br = np.float32([-sys.maxint - 1, -sys.maxint - 1])
bl = np.float32([sys.maxint, -sys.maxint - 1])

height, width = sample_mask.shape

for w in range(width):
    for h in range(height):
        if t1[0] == 1:
            pass

print(sample_mask.shape)