import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("picture.csv")
data = df.values
A = 500
B = 500
W = 5
N = 5000
M = 1.5
rng = np.random.default_rng()
fig = plt.figure(figsize=(6, 6))
xl = []
xr = []
y = []
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
for i in range(N):
    xp = rng.uniform(0, len(data[0]))
    yp = rng.uniform(0, len(data))
    zp = M * data[int(yp)][int(xp)]
    xp = xp - len(data[0]) / 2
    yp = yp - len(data) / 2
    xl.append( (- 0.5 * W * (A + zp) + B * xp) / (A + B - zp))
    xr.append( (+ 0.5 * W * (A + zp) + B * xp) / (A + B - zp))
    y.append( B * yp / (A + B - zp))
    
ax1.scatter(xl, y, color="#000000", s=1)
ax2.scatter(xr, y, color="#000000", s=1)
ax1.set_xlim(-0.25*len(data[0]), 0.25*len(data[0]))
ax1.set_ylim(-0.25*len(data), 0.25*len(data))
ax2.set_xlim(-0.25*len(data[0]), 0.25*len(data[0]))
ax2.set_ylim(-0.25*len(data), 0.25*len(data))
plt.savefig("RDS.png")
plt.show()