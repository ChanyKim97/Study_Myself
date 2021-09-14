import numpy as np

array1 = np.array([2,3,5,7,11,13,17,19])

print(array1>4)

print(array1 % 2 ==0)

booleans = np.array([True,True,False,True,False,True,False])
print(np.where(booleans))

filterr = np.where(array1>4)
print(array1[filterr])