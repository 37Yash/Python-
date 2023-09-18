import numpy as np;

arr=np.array([1,2,3,4,5,6,7,8,9])
arr1=np.reshape(arr,(3,3))
s=0
for i in range(0,3):
    for j in range(0,3):
        if(i==j):
            s+=arr1[i][j]

print("sum=",s)
