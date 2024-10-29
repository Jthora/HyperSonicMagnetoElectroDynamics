import numpy as np
import matplotlib.pyplot as plt

# Parameters for spin wave with damping
initial_amplitude = 1.0  # Initial amplitude of spin wave
damping_constant = 0.1  # Damping factor (controls rate of dissipation)
frequency = 15  # Spin wave frequency (Hz)
time = np.linspace(0, 2, 500)  # 2 seconds

# Spin wave with exponential damping
damped_wave = initial_amplitude * np.exp(-damping_constant * time) * np.sin(2 * np.pi * frequency * time)

# Energy dissipation (proportional to amplitude squared)
energy_dissipation = damped_wave**2

# Visualization
plt.figure(figsize=(10, 5))
plt.subplot(2, 1, 1)
plt.plot(time, damped_wave, label="Damped Spin Wave", color="blue")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Spin Wave with Energy Dissipation")
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(time, energy_dissipation, label="Energy Dissipation", color="red")
plt.xlabel("Time (s)")
plt.ylabel("Energy Dissipation")
plt.legend()
plt.tight_layout()
plt.show()
