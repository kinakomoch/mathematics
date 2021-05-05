import numpy as np

A = np.zeros((3, 3), dtype=np.complex)
A =([complex(2, 0), complex(0, -1) , complex(-1, 0)]
,[complex(-1, 0), complex(1, 1), complex(-1, 0)],
[complex(0, 0), complex(-1, 0), complex(3, 0)])

detA = np.linalg.det(A)
print(detA)
