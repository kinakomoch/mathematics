import numpy as np

def fc_high(r,c):
    fc = 1 / (2 * np.pi * c * r)

    return fc

def fc_low(r, l):
    fc = r / (2 * np.pi * l)

    return fc

def relative_error(real, ideal):
    err = (real - ideal) / ideal

    return err


if __name__ == '__main__':
    f_high400 = fc_high(400, 0.33 * 10 **(-6))
    err_h400 = relative_error(1000, f_high400)
    f_low400 = fc_low(400, 123 * 10 **(-3))
    err_l400 = relative_error(600, f_low400)
    print('R=400ohm\n')
    print('high\t{0}Hz\terror = {1}\n'.format(f_high400, err_h400))
    print('low\t{0}Hz\terror = {1}\n'.format(f_low400, err_l400))

    f_high600 = fc_high(600, 0.33 * 10 **(-6))
    err_h600 = relative_error(640, f_high600)
    f_low600 = fc_low(600, 123 * 10 **(-3))
    err_l600 = relative_error(920, f_low600)
    print('R=600ohm\n')
    print('high\t{0}Hz\terror = {1}\n'.format(f_high600, err_h600))
    print('low\t{0}Hz\terror = {1}\n'.format(f_low600, err_l600))

    f_high1000 = fc_high(1000, 0.33 * 10 **(-6))
    err_h1000 = relative_error(560, f_high1000)
    f_low1000 = fc_low(1000, 123 * 10 **(-3))
    err_l1000 = relative_error(1100, f_low1000)
    print('R=1000ohm\n')
    print('high\t{0}Hz\terror = {1}\n'.format(f_high1000, err_h1000))
    print('low\t{0}Hz\terror = {1}\n'.format(f_low1000, err_l1000))
