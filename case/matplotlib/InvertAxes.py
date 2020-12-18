import matplotlib.pyplot as plt
import numpy as np

t = np.arange(-1, 5.0, 0.01)
s = np.exp(t)

fig, ax = plt.subplots()

ax.plot(t, s)
ax.set_xlim(-1,5)  # decreasing time
ax.set_xlabel('decreasing time (s)')
ax.set_ylabel('voltage (mV)')
ax.set_title('Should be growing...')
ax.grid(True)

plt.show()