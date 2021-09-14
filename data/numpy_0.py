import numpy

array1 = numpy.array([2,3,4,5,13,15,16,17,27])

print(type(array1))
print(array1.shape)

array2 = numpy.array([[2,3,4],[5,13,15],[16,17,27]])

print(type(array2))
print(array2.shape)

array3 = numpy.full(5, 10)
print(array3)

array4 = numpy.random.random(6)
print(array4)

array5 = numpy.arange(2,6,2)
print(array5)

array6 = numpy.ones(7, dtype=int)
print(array6)