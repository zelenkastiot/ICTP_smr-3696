#!/usr/bin/env python

from ctypes import *

# import DSO
dso = CDLL("./hello.so")
dso.hello.argtypes = [c_char_p]

print ("Calling DSO")
dso.hello(b'World')

buf = create_string_buffer(b"World");
print ("Calling DSO with buffer")
dso.hello(buf)
print ("Done")

