import numpy
N,M = map(int, input().split())
arr = numpy.array([list(map(int,(input().split()))) for i in range(N)])

print(numpy.max(numpy.min(arr,axis = 1)))