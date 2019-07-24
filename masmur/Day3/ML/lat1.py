import numpy as np  

np_array = np.array(
    [
        [0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
        [10, 11, 12, 13, 14]
    ]
)

# print(np_array.ndim, np_array.shape)
# print(np_array)

# array_zero = np.zeros((3,4))
# print(array_zero.ndim, array_zero.shape) 
# print(array_zero)


#Array 3 dimensi dengan 2 baris x 3 kolom x 
# array_ones = np.ones((2,3,4), dtype = np.int16)
# print(array_ones) 

#array kosong 2 x 3
# array_kosong = np.empty((2,3))
# print(array_kosong)


# menciptakan array dengan pola tertentu
# Array 1D dengan bilangan dari 1 s/d 30 dengan kenaikan 5
# array_1d = np.arange(10, 30, 5)
# print(array_1d)

# Array 1D dengan bilangan dari 0 s/d 2 dengan kenaikan 0.3
# array_1d = np.arange(0, 2, 0.3)
# print(array_1d)

# Membuat array 1S dengan 9 bilangan, dengan jarak merata 
array_1d = np.linspace(0, 2, 9)
print(array_1d)
print(array_1d.ndim, array_1d.shape) 


