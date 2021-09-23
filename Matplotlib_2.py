import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,5,11)
y = x**2

fig,ax = plt.subplots(figsize=(8,4))
ax.plot(x,x**2,label='X Square')
ax.plot(x,x**3,label='X cube')
ax.legend(loc=0)
ax.set_xlim([0,2])
ax.set_ylim([0,2])
plt.show()