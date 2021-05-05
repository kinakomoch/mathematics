#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
フーリエ級数図の変化

"""

import numpy as np
import matplotlib.pyplot as plt

def f(n):
    x = np.linspace(-2*np.pi, 2*np.pi, 2560, endpoint=True)
    f = 0.5
    for k in range(1, n):
        f += (1- (-1)**k) / k / np.pi * np.sin(k * x)

    plt.plot(x, f)
    plt.ylim((0, 2))
    plt.show()

if __name__ == '__main__':
    f(300)
