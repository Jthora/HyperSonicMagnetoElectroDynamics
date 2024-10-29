import numpy as np
import matplotlib.pyplot as plt

# Parameters
speed_of_sound = 5e3  # m/s
k_values = np.linspace(-np.pi, np.pi, 200)  # Wave vectors

# Dispersion relation
omega_acoustic = speed_of_sound * k_values
omega_optical = np.sqrt(speed_of_sound**2 * k_values**2 + (1e12)**2)  # Arbitrary optical mode

# Plot
plt.figure()
plt.plot(k_values, omega_acoustic, label="Acoustic Phonon")
plt.plot(k_values, omega_optical, label="Optical Phonon")
plt.xlabel("Wave Vector (k)")
plt.ylabel("Frequency (ω)")
plt.title("Phonon Dispersion Relation")
plt.legend()
plt.grid()
plt.show()
