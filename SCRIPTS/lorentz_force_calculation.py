import numpy as np
import matplotlib.pyplot as plt

# Parameters
charge = 1.6e-19  # Charge of the particle (Coulombs)
velocity = np.array([2.0, 0.0, 0.0])  # Velocity vector (m/s)
magnetic_field = np.array([0.0, 0.0, 1.0])  # Magnetic field vector (Tesla)

# Lorentz force calculation: F = q * (v x B)
lorentz_force = charge * np.cross(velocity, magnetic_field)

# Output
print(f"Lorentz force on the particle: {lorentz_force} N")

# Visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(0, 0, 0, *velocity, color='b', label='Velocity')
ax.quiver(0, 0, 0, *magnetic_field, color='r', label='Magnetic Field')
ax.quiver(0, 0, 0, *lorentz_force, color='g', label='Lorentz Force')
plt.legend()
plt.title('Lorentz Force Calculation')
plt.show()
