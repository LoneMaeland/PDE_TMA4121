import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

Lx = Ly = 1.0  # lengde av platen i x- og y-retning
T = 1.0  # total tid
Nx = Ny = 100  # antall steg i x- og y-retning
Nt = 1000  # antall tidssteg
alpha = 0.01  # termisk diffusivitet
dx = dy = Lx / Nx  # steglengde i x- og y-retning
dt = T / Nt  # tidssteg

# Initialbetingelse: en varm plate med en varmekilde i midten
u = np.zeros((Nx, Ny))
u[Nx//2, Ny//2] = 1.0  # varmekilden er i midten av platen

for n in range(Nt):
    for i in range(1, Nx-1):
        for j in range(1, Ny-1):
            u[i, j] += alpha * dt / dx**2 * (u[i-1, j] - 2*u[i, j] + u[i+1, j]) + \
                       alpha * dt / dy**2 * (u[i, j-1] - 2*u[i, j] + u[i, j+1])



x = np.linspace(0, Lx, Nx)
y = np.linspace(0, Ly, Ny)
X, Y = np.meshgrid(x, y)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, u, cmap='inferno')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Temperatur')
ax.set_title('Løsning av varmeligningen i to dimensjoner')
plt.show()

