import numpy as np
N,M = map(int, input().split(' '))

arr1=[]
for i in range(N):
    arr1.append(list(map(int, input().split(' '))))
arr1=np.array(arr1)
arr2 =[]
for i in range(N):
    arr2.append(list(map(int, input().split(' '))))
arr2= np.array(arr2)

print(np.add(arr1,arr2))
print(np.subtract(arr1,arr2))
print(np.multiply(arr1,arr2))
print(np.floor_divide(arr1,arr2))
print(np.mod(arr1,arr2))
print(np.power(arr1,arr2))
