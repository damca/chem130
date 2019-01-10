import numpy as np
import matplotlib.pyplot as plt

plt.switch_backend('tkagg')

N = 210 # number of particles
nstep = 4000
n = np.zeros(nstep)
n[0] = N
for i in range(1, nstep):
    r = np.random.rand() # get a random number in [0, 1]
    if r < n[i-1]/N:
        n[i] = n[i-1] - 1
    else:
        n[i] = n[i-1] + 1

fig, ax = plt.subplots()
ax.plot(np.arange(nstep), n)
ax.set_xlabel("Time")
ax.set_ylabel("n")
ax.set_yticks(range(50, 251, 50))
plt.show()
fig.savefig("ps1 n(t).svg")


