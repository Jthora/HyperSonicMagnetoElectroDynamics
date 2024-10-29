import numpy as np
import matplotlib.pyplot as plt

# Spin wave parameters
frequency = 10  # Frequency of the primary spin wave (Hz)
amplitude = 1.0  # Amplitude of the primary spin wave
lattice_positions = np.linspace(0, 10, 500)  # 1D array of lattice positions (arbitrary units)
time = 0.1  # Time snapshot (s)

# Primary spin wave
primary_wave = amplitude * np.sin(2 * np.pi * frequency * time - lattice_positions)

# Counter wave (opposite phase)
counter_amplitude = amplitude  # Set equal amplitude for maximum interference
counter_frequency = frequency
phase_shift = np.pi  # 180 degrees out of phase for destructive interference
counter_wave = counter_amplitude * np.sin(2 * np.pi * counter_frequency * time - lattice_positions + phase_shift)

# Resulting wave (combined effect)
resulting_wave = primary_wave + counter_wave

# Visualization
plt.figure()
plt.plot(lattice_positions, primary_wave, label="Primary Spin Wave", color="blue")
plt.plot(lattice_positions, counter_wave, label="Counter Wave (Opposite Phase)", color="red")
plt.plot(lattice_positions, resulting_wave, label="Resulting Wave (Destructive Interference)", color="green", linestyle="--")
plt.xlabel("Lattice Position")
plt.ylabel("Amplitude")
plt.title("Spin Wave Phase Cancellation")
plt.legend()
plt.show()
