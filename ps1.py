# organized energy tends towards disorganized energy

import numpy as np
import matplotlib.pyplot as plt

n = 10
k = 1e5 # interspring constant
kw = 1e6 # wall spring constant
d = 0.1 # overll distance of masses in meters
m = 0.1 # kilograms
t = 20.0 # seconds
g = 9.81
z0 = 0.1 # initial height
dt = 1e-4 # timestep
nstep = int(round(t / dt))
print("number of steps:", nstep)
z = np.zeros((n, nstep), float)
vz = np.zeros((n, nstep), float)
z[:, 0] = d * np.arange(n) / n + z0 # initial positions
print("initial positions:", z[:,0])
dl = d / n
for i in range(1, nstep):
    dz = np.diff(z[:, i-1]) - dl # positive values if interspring distance larger than equilibrium
    f_down = -k * np.append(0.0, dz) 
    f_up = k * np.append(dz, 0.0)
    f = f_down + f_up - m*g
    f[0] = f[0] - kw*z[0, i-1] * (z[0, i-1] < 0)
    a = f / m
    vz[:, i] = vz[:, i-1] + a * dt
    z[:, i] = z[:, i-1] + vz[:, i]*dt
print(z)

fig, ax = plt.subplots()
ax.plot(np.arange(0, t, dt), z.mean(axis=0))
fig.savefig('test.pdf')

# conceptual problem, why does the code break if dt=1e-2 ?
# 
