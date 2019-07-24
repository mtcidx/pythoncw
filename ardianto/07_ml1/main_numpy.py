import numpy as np

np_array = np.array([
    [0, 1, 2, 3, 4],
    [5, 6, 7, 8, 9],
    [10, 11, 12, 13, 14]
])

print(np_array.ndim, np_array.shape)

# hanya ukuran yang diketahui
array_zero = np.zeros((3, 4))
print(array_zero.ndim, array_zero.shape)
print(array_zero)

#
array_ones = np.ones((2, 3, 4), dtype=np.int16)
print(array_ones)

# initialisasi
array_kosong = np.empty((2, 3), dtype=np.int16)
print(array_kosong)

# Array 1D dengan bilangan
array_1d = np.arrange(10, 30, 5)

# Array 1D dengan bilangan
array_1d = np.arrange(0, 2, 0.3)

# Membuat array 1D dengan 9 bilangan, jarak merata

array_1d = np.linspace(0, 2, 9)
print(array_1d)
print(array_1d.ndim, array_1d.shape)
