import numpy as np
np.set_printoptions(legacy = '1.13')
N = np.array([float(i) for i in input().split()])   
print(np.floor(N),np.ceil(N), np.rint(N),sep="\n")