import numpy as np

np_array = np.array(
    [
        [0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
        [10, 11, 12, 13, 14],
    ]
)
# Ukurannya 3 x 5
print(np_array.ndim, np_array.shape)
# np_array_2d = np.array(
#     [
        
#     ]
# )
array_zero = np.zeros((3,4))
print(array_zero.ndim, array_zero.shape)
print(array_zero)

array_ones = np.ones((2, 3, 4), dtype=np.int16)
print(array_ones)
# 2 tinggi, 3 baris, 4 kolom

array_kosong = np.empty((2,3), dtype=int)
print(array_kosong)

array_1d = np.arange(10, 30, 5)
print(array_1d)
array_1d = np.arange(0, 2, 0.3)
print(array_1d)

array_1d = np.linspace(0, 2, 9)
print(array_1d)
print(array_1d.ndim, array_1d.shape)