'''
複素行列の逆行列計算
'''


import numpy as np

A = 0.5
B = -1.5j
C = -0.5j
D = 0.5

Z1 = 1 + 1.0j
Z2 = 1 - 1.0j

array = np.zeros((2, 2), dtype=np.complex)
array[0][0] = A + Z1 * C
array[0][1] = B + Z1 * D
array[1][0] = 1
array[1][1] = - Z2

inv_array = np.linalg.inv(array)

print(inv_array)
