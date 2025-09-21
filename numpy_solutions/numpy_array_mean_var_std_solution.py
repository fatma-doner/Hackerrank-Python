import numpy as np
N,M = map(int, input().split())
arr1 = np.array([list(map(int, input().split())) for i in range(N)])
print(np.mean( arr1,axis= 1))
print(np.var( arr1, axis = 0))
print(round(np.std(arr1,axis = None),11))
