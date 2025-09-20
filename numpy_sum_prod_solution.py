import numpy as np

N,M = map(int,input().split())
list1 =[]
for i in range(N):
    A = list(map(int,input().split()))
    list1.append(A)
arr1 = np.array(list1)
print(np.prod(np.sum(arr1,axis = 0)))

