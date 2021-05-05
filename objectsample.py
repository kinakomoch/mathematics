import numpy as np

class jikkenb4:
    def __init__(self, resistance, capacitor, inductor):
        self.res = resistance #抵抗値
        self.cap = capacitor #コンデンサ静電容量
        self.ind = inductor #コイルの値

    def f0(self):
        one = 1 / (2 * np.pi)
        two = 1 / np.sqrt(self.ind * self.cap)
        three = self.res **2 * self.cap / self.ind
        f0 = one * two * np.sqrt(-three + np.sqrt(1 + 2 * three))

        return f0

    def zabsmax(self):
        w0 = 2 * np.pi * self.f0()
        denominator = (1 - (w0 **2) * self.cap * self.ind) **2 + (w0 * self.cap * self.res) **2
        numerator = self.res **2 + (w0 **2) * (self.ind **2)
        zabs = np.sqrt(numerator / denominator)

        return zabs

    def f1f2(self):
        a = self.cap * self.ind
        b = 0.5 * (self.cap * self.res) **2 - self.cap * self.ind - (self.ind / self.zabsmax()) ** 2
        c = 1 - 2 * (self.res / self.zabsmax()) **2
        root = np.sqrt(b **2 - c * (a **2) )
        f1 = (1 / (2 * np.pi)) * np.sqrt(- b - root) / a
        f2 = (1 / (2 * np.pi)) * np.sqrt(- b + root) / a

        return f1, f2

if __name__ == '__main__':
    print('\n')
    jikken = jikkenb4(3.612, 1*10**(-6), 10*10**(-3))
    print('f0の値は{0}'.format(jikken.f0()))
    print('zmaxの値は{0}'.format(jikken.zabsmax()))
    print(jikken.f1f2())
    print('\n')
    r20 = jikkenb4(22.16, 1*10**(-6), 10*10**(-3))
    print('f0の値は{0}'.format(r20.f0()))
    print('zmaxの値は{0}'.format(r20.zabsmax()))
    print(r20.f1f2())
    print('\n')
    r51 = jikkenb4(53.44, 1*10**(-6), 10*10**(-3))
    print('f0の値は{0}'.format(r51.f0()))
    print('zmaxの値は{0}'.format(r51.zabsmax()))
    print(r51.f1f2())
    print('\n')
