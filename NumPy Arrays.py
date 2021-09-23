import numpy as np

# l = [[1 , 2 , 3],[4 , 5 , 6],[7 , 8 , 9]]
# arr = np.array(l)
# print(arr)
# print(arr.flatten())
# print(arr.reshape(3,3))
# print(arr.max())
# print(arr.min())
# print(arr.argmax())
# print(arr.argmin())
# print(arr.shape)

# arr = np.zeros((4,4))
# print(arr)

# arr = np.ones(5)

# arr = np.arange(1,10,2)
# print(arr)

# arr = np.linspace(1 , 10 , 20)
# print(arr)

# arr = np.eye(3) #create identity matrix
# print(arr)
#
# arr = np.random.rand(5)
# print(arr)
# arr = np.random.rand(2,2)
# print(arr)

# arr = np.random.randint(0,100)
# print(arr)
# arr = np.random.randint(0,100,10)
# print(arr)

# arr = np.arange(1, 11)
# print(arr)
# print(arr[5])
# print(arr[7:3])
# arr[0:5]=100
# print(arr)

# arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr_2d)
# print()
# print(arr_2d[1][0])
# print(arr_2d[1,0])

arr = np.arange(0,11)
print(arr)
bool_arr = arr>5
print(bool_arr)
print(arr[bool_arr])
print(arr[arr>5])

# create an array of ten five

a  = np.ones(10) *5
print(a)