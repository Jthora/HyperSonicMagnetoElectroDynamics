import numpy as np
import matplotlib.pyplot as plt

# Parameters
exchange_constant = 1.0  # Arbitrary units
spin = 0.5  # Spin quantum number
lattice_spacing = 0.5  # Distance between atoms

# Wave vector range
k_values = np.linspace(-np.pi / lattice_spacing, np.pi / lattice_spacing, 200)

# Magnon dispersion relation
omega_magnon = 2 * exchange_constant * spin * (1 - np.cos(k_values * lattice_spacing))

# Plot
plt.figure()
plt.plot(k_values, omega_magnon, label="Magnon Spin Wave Dispersion")
plt.xlabel("Wave Vector (k)")
plt.ylabel("Frequency (ω)")
plt.title("Magnon Spin Wave Dispersion Relation")
plt.legend()
plt.grid()
plt.show()
