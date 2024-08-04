import numpy as np

arr1=np.array([3,21,4,5])
arr2=np.array([2,1,3,4])


arr=np.vstack((arr1,arr2))


sorted_indices=np.argsort(arr2)

cols=sorted_indices
sorted_arr=arr[:,cols]
print(sorted_arr)