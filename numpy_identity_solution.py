import numpy
numpy.set_printoptions(legacy='1.13')
N,M = map(int, input().split())
eye = numpy.eye(N,M,k=0)
print(eye)
