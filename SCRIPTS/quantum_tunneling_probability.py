import numpy as np

# Parameters
mass = 9.11e-31  # Mass of electron (kg)
barrier_height = 1e-18  # Potential barrier height (J)
barrier_width = 1e-9  # Width of the barrier (m)
energy = 0.8e-18  # Energy of the particle (J)
h_bar = 1.0545718e-34  # Reduced Planck constant (J.s)

# Tunneling probability
kappa = np.sqrt(2 * mass * (barrier_height - energy)) / h_bar
tunneling_probability = np.exp(-2 * kappa * barrier_width)

# Output
print(f"Tunneling probability: {tunneling_probability:.4e}")
