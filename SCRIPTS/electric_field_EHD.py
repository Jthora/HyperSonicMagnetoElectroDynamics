import numpy as np
import matplotlib.pyplot as plt

# Grid parameters
grid_size = 50
voltage = 5.0  # Voltage applied (V)
distance = 10  # Distance between electrodes (mm)
spacing = 0.2  # mm

# Electric field calculation
x, y = np.meshgrid(np.linspace(-grid_size, grid_size, 100), np.linspace(-grid_size, grid_size, 100))
E_x = voltage / distance * (y / np.sqrt(x**2 + y**2))
E_y = voltage / distance * (x / np.sqrt(x**2 + y**2))

# Visualization
plt.figure()
plt.streamplot(x, y, E_x, E_y, color=np.sqrt(E_x**2 + E_y**2), cmap='inferno')
plt.colorbar(label="Electric Field Strength (V/mm)")
plt.title("Electric Field in EHD Setup")
plt.xlabel("x (mm)")
plt.ylabel("y (mm)")
plt.show()
