import numpy as np
import matplotlib.pyplot as plt

e = 10
R = 10
L = 1*10**(-3)
C = 1*10**(-6)

f = np.logspace(1*10**(-6), 8, 1000)

w = 2*np.pi*f
z = 1.0/(1.0/(w*L*1.0j)+(w*C*1.0j)/(w*C*R*1.0j+1.0))
zabs = np.abs(z)
zang = np.angle(z)
plt.plot(f, zabs)
#plt.plot(f, zang)

ax = plt.gca()
ax.spines['top'].set_color('none')

ax.set_xscale('log')  # メイン: x軸をlogスケールで描く
ax.set_xscale('log')

#plt.title('single logarithmic plot')
#plt.xlabel('f',fontsize=18)
#plt.ylabel('zabs',fontsize=18)

#plt.grid(which="both") # グリッド表示。"both"はxy軸両方にグリッドを描く。
#plt.polar(zang, zabs)
plt.show()
