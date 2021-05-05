import math
import numpy as np
import matplotlib.pyplot as plt

N = 3542
l = 0.10
a2 = 0.053
a1 = 0.009

def jikken(I1, I2, color1, color2):
    x = np.arange(-0.10, 0.10, 0.0001)
    da = a2 - a1
    one = N * I1 / (2 * l * da)
    one2 = N * I2 / (2 * l * da)
    naka1 = (a2 + np.sqrt(a2**2 + x**2)) / (a1 + np.sqrt(a1**2 + x**2))
    naka2 = (a2 + np.sqrt(a2**2 + (l - x)**2)) / (a1 + np.sqrt(a1**2 + (l -x) **2))
    two = x * np.log(naka1) + (l - x) * np.log(naka2)
    H1 = one * two
    H2 = one2 * two
    plt.plot(x, H1, color1)
    plt.plot(x, H2, color2)
    plt.show()

if __name__ == '__main__':
    jikken(1.0, 0.5, "r", "b")
