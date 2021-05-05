#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
電圧の挙動チェック

"""

import math
import numpy as np
import matplotlib.pyplot as plt

def volt(vmax, delta, color):

    t = np.arange(0, 0.01, 0.000000001)
    x = 200 * np.pi * t + delta
    vt = vmax * np.sin(x)
    plt.plot(t, vt, color)


if __name__ == '__main__':
    volt(2, 0, "r")
    #volt(1, np.pi/4, "b")
    volt(1, -np.pi/3, "g")
    plt.show()
