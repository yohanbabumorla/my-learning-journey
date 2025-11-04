import numpy as np

a = np.array([1,2,3])
print(a)
b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(b)
#get dimension
print(a.ndim)
print(b.ndim)
#get shape
print(a.shape)
print(b.shape)
#get type
print(a.dtype,b.dtype)
b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b[0,0,0])
a = np.zeros(5)
print(a)