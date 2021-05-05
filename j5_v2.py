import numpy as np

def low_ratio(fc):
    f = 0
    flist = {}
    for i in range(19):
        if 1000 <= f:
            f += 1000
        elif f < 1000:
            f += 100
        key = f
        ratio = - 10 * np.log10((1 - (f/fc)**2)**2 + (f/fc)**2)
        flist[key] = ratio

    return  flist

def high_ratio(fc):
    f = 0
    flist = {}
    for i in range(19):
        if 1000 <= f:
            f += 1000
        elif f < 1000:
            f += 100
        key = f
        ratio = 20 * np.log10((f/fc)**2)- 10 * np.log10((1 - (f/fc)**2)**2 + (f/fc)**2)
        flist[key] = ratio

    return  flist

def low_phase(fc):
    f = 0
    flist = {}
    for i in range(19):
        if 1000 <= f:
            f += 1000
        elif f < 1000:
            f += 100
        key = f
        if f != fc:
            phase = - np.arctan((f/fc)/(1 - (f/fc)**2))
            phase = np.rad2deg(phase)
        else:
            phase = -90
        if phase > 0:
            phase -= 180

        flist[key] = phase


    return flist

def high_phase(fc):
    f = 0
    flist = {}
    for i in range(19):
        if 1000 <= f:
            f += 1000
        elif f < 1000:
            f += 100
        key = f
        if f != fc:
            phase = - np.arctan((f/fc)/(1 - (f/fc)**2))
            phase = np.rad2deg(phase) + 180
        else:
            phase = 90
        if phase > 180:
            phase -= 180

        flist[key] = phase


    return flist

if __name__ == '__main__':
    flist_low = low_ratio(2000)
    flist_high = high_ratio(500)
    phase_low = low_phase(2000)
    phase_high = high_phase(500)

    import pprint
    pp = pprint.PrettyPrinter()
    print('LPF\n')
    print('Voltage transmission ratio\t')
    pp.pprint(flist_low)
    print('\nPhase\t')
    pp.pprint(phase_low)
    print('\n')

    print('HPF')
    print('Voltage transmission ratio\t')
    pp.pprint(flist_high)
    print('\nPhase\t')
    pp.pprint(phase_high)
