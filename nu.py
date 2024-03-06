import numpy as np

arr = np.array([5,6,7], np.int8)
print(arr)
print(arr[1])

arr2 = np.array([[1,6,3],[4,7,8],[9,7,8]])
arr3= np.array([[[9,7,5],[7,5,1],[6,4,5]]])

print(arr2)
print(arr2[2,1])
print(arr2[2])

print(arr.shape) #1D array with 3 length
print(arr2.shape) #2d array with 3 columns and 3 rows

zeros = np.zeros([3,3])
print(zeros)

range = np.arange(10)
print(range)

lspace = np.linspace(1,10,2)
print(lspace)

print(arr2.T)
print(arr3.ndim)


arr4 = np.array([[1,9],[4,6],[2,5]])
print(arr4)
arr4 = arr4.reshape(2,3)
print(arr4)