import numpy as np
import matplotlib.pyplot as plt

# Spin wave parameters
primary_frequency = 20  # Frequency of primary spin wave (Hz)
primary_amplitude = 1.0  # Amplitude of primary wave

# Counter wave parameters
counter_frequency = primary_frequency * 1.02  # Small offset to create dephasing
counter_amplitude = 1.0

# Time array for observation
time = np.linspace(0, 1, 1000)  # Observation over 1 second

# Primary and counter spin waves
primary_wave = primary_amplitude * np.sin(2 * np.pi * primary_frequency * time)
counter_wave = counter_amplitude * np.sin(2 * np.pi * counter_frequency * time)

# Resulting signal (dephasing over time)
resulting_wave = primary_wave + counter_wave

# Visualization
plt.figure()
plt.plot(time, primary_wave, label="Primary Spin Wave", color="blue")
plt.plot(time, counter_wave, label="Counter Wave (Offset Frequency)", color="red", linestyle="--")
plt.plot(time, resulting_wave, label="Resulting Wave (Dephased)", color="green")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Spin Wave Resonance Disruption through Dephasing")
plt.legend()
plt.show()
