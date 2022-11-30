# Task 2: User input 
import sys
import numpy as np
import matplotlib.pyplot as plt

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]



# print ("Number of arguments:", len(sys.argv), "arguments")
print(sys.argv)

x = float(sys.argv[2])
y = float(sys.argv[1])

data = np.fromfile('data.bsq', dtype='uint8')

# data = np.memmap('data.bsq',
                #  mode='r',
                #  shape=(21600,43200)
                # )

data = data.reshape(21600, 43200) 

la_x = np.linspace(-180, 180, 43200)  
la_y = np.linspace(90, -90, 21600)    

print(np.shape(la_x), np.shape(la_y))

my_x = np.argwhere(la_x == find_nearest(la_x, x))[0][0]
my_y = np.argwhere(la_y == find_nearest(la_y, y))[0][0]

print(find_nearest(la_x, x), my_x,  find_nearest(la_y, y), my_y)

print(data[my_y][my_x])
if data[my_y][my_x] == 0:
    print('Water')
else:
    print("Land")