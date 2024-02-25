import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr[2] + arr[3])

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
arr1 = np.array(42)
print(arr1)
print(arr)
print(np.__version__)
print(type(arr))

import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
 

print(arr[0, 1, 2])
print("array:", arr[:4])