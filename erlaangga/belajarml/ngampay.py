import numpy as np

np_arr = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print('Dimensi: %d dan bentuk %s' %(np_arr.ndim, np_arr.shape))

np_zero = np.zeros((3,4))
print(np_zero.ndim, np_zero.shape)

np_one = np.ones((2,3,4), dtype=np.int16)
print(np_one.ndim, np_one.shape)

np_empty = np.empty((2,3), dtype=None)
print(np_empty.ndim, np_empty.shape)

np_arrange = np.arange(10,30,5)

np_linspace = np.linspace(0,2,9)
print(np_linspace)

