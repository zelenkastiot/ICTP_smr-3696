# Task 1: Map locations
import numpy as np
import matplotlib.pyplot as plt


data = np.fromfile('data.bsq', dtype='uint8')

# data = np.memmap('data.bsq',
                #  mode='r',
                #  shape=(21600,43200)
                # )

data = data.reshape(21600, 43200) # Resize: 43200 Pixels x 21600 Lines 

print('data', data)
print('minmax', data.min(), data.max())
print('shape', data.shape)

plt.imshow(data[::50, ::50], cmap='hot')
plt.show()



