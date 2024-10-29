import numpy as np
import matplotlib.pyplot as plt

# Primary spin wave parameters
spin_wave_frequency = 15  # Hz
amplitude = 1.0  # Amplitude of spin wave

# External field modulation parameters
field_base_frequency = 15  # Base frequency of external field (matches spin wave)
modulation_frequency = 1  # Frequency of modulation (Hz)
modulation_depth = 0.5  # Depth of modulation

# Time array for simulation
time = np.linspace(0, 2, 500)  # 2 seconds

# Spin wave signal
spin_wave = amplitude * np.sin(2 * np.pi * spin_wave_frequency * time)

# Modulated external field
modulated_field = amplitude * (1 + modulation_depth * np.sin(2 * np.pi * modulation_frequency * time)) * np.sin(2 * np.pi * field_base_frequency * time)

# Resulting signal after interference
resulting_signal = spin_wave - modulated_field  # Assuming counteraction by modulation

# Visualization
plt.figure()
plt.plot(time, spin_wave, label="Primary Spin Wave", color="blue")
plt.plot(time, modulated_field, label="Modulated Counter Field", color="red", linestyle="--")
plt.plot(time, resulting_signal, label="Resulting Signal", color="green")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Spin Wave Field Modulation Countermeasure")
plt.legend()
plt.show()
