#!/usr/bin/env python

from ctypes import *
from math import *

# import DSO
dso = CDLL("./sum.so")

# fill data structure
num = 10
ilist = (c_int * num)()
for i in range(num):
   ilist[i] = i*i

print ("Calling DSO with ints")
dso.sum_of_ints.argtypes = [ POINTER(c_int), c_int ]
dso.sum_of_ints.restype = c_int
isum = dso.sum_of_ints(ilist,num)
print ("Integer sum is: ", isum)

########
# fill data structure
dlist = (c_double * num)()
for i in range(num):
   dlist[i] = 0.333*(i+0.5)

print ("Calling DSO with doubles")
dso.sum_of_doubles.argtypes = [ POINTER(c_double), c_int ]
dso.sum_of_doubles.restype = c_double
dsum = dso.sum_of_doubles(dlist,num)
print ("Doubles sum is: ", dsum)
