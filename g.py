import numpy as np
import matplotlib.pyplot as plt

def function():
    r = np.arange(1, 2.1, 0.1)
    x = np.arange(-1, 3, 0.1)
    R, X = np.meshgrid(r, x)
    Z = (R - 1) * X * X - (2 - R) * (3-2*R) * (3-2*R)
    plt.contour(R, X, Z, [0])
    plt.show()

if __name__ == '__main__':
    function()
