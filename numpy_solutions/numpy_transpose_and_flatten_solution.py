import numpy
N,M = map(int, input().split())
A = numpy.array([input().split() for i in range(N)], dtype = int)
print(numpy.transpose(A))
print(A.flatten())
