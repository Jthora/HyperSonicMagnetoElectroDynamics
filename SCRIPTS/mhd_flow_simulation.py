import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
size = 100
magnetic_field = 0.1  # Tesla
viscosity = 0.02
time_steps = 100
dt = 0.01

# Initialize velocity field
u = np.zeros((size, size))
v = np.zeros((size, size))
B = magnetic_field * np.ones((size, size))

# MHD effect on fluid flow
for _ in range(time_steps):
    u[1:-1, 1:-1] += dt * (viscosity * (u[2:, 1:-1] - 2*u[1:-1, 1:-1] + u[:-2, 1:-1]) +
                           B[1:-1, 1:-1] * v[1:-1, 1:-1])
    v[1:-1, 1:-1] += dt * (viscosity * (v[1:-1, 2:] - 2*v[1:-1, 1:-1] + v[1:-1, :-2]) -
                           B[1:-1, 1:-1] * u[1:-1, 1:-1])

# Visualization
plt.figure()
plt.quiver(u, v, scale=1.5)
plt.title("MHD Flow Simulation in a 2D Channel")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
