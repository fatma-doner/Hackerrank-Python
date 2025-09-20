import numpy
N,M,P = map(int,input().split()) 
list1 =[]
list2 = []
for i in range(N):
    arr1 = list(map(int,input().split()))
    list1.append(arr1)
    
for i in range(M):
    arr2 = list(map(int,input().split()))
    list2.append(arr2)
    
print(numpy.concatenate((numpy.array(list1),numpy.array(list2))))