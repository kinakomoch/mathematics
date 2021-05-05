#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
フーリエ級数の図の変化

"""

import numpy as np
import matplotlib.pyplot as plt

def f(n):
    x = np.linspace(-2*np.pi, 2*np.pi, 2560, endpoint=True)
    f = 0.25 * np.pi
    for k in range(1, n):
        f += ((-1)**k - 1) / (k**2) / np.pi * np.cos(k * x) + (-1)**(k+1) / k * np.sin(k * x)

    plt.plot(x, f)
    plt.ylim((-1, 4))
    plt.show()

if __name__ == '__main__':
    f(100)
