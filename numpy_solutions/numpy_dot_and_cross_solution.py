import numpy as np

N = int(input())
A = np.array([input().split() for _ in range(N)], int)
B = np.array([input().split() for _ in range(N)],int)
#A = np.array([list(map(int,input().split())) for i in range(N)])
#B = np.array([list(map(int,input().split())) for i in range(N)])
print(A@B)
#print(np.dot(A,B))