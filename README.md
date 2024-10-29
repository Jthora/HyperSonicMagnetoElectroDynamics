# HyperSonicMagnetoElectroDynamics
The dynamics between Sound, Magnetism and Electricity (Phonons, Magnons and Electrons)


# Magnetic and Electric and Sonic Dynamics Equations (MHD, EHD, Phonons, Magnons, and Electrons)

---

## Magnetic Dynamics Equations (MHD)
1. **Navier-Stokes with Lorentz Force** (for fluid in magnetic fields):
   \[
   \rho \left( \frac{\partial \mathbf{v}}{\partial t} + (\mathbf{v} \cdot \nabla) \mathbf{v} \right) = -\nabla p + \eta \nabla^2 \mathbf{v} + \mathbf{J} \times \mathbf{B}
   \]
   - \(\rho\): Fluid density, \(\mathbf{v}\): Velocity, \(\mathbf{J}\): Current density, \(\mathbf{B}\): Magnetic field

2. **Magnetic Induction Equation** (for time evolution of \(\mathbf{B}\)):
   \[
   \frac{\partial \mathbf{B}}{\partial t} = \nabla \times (\mathbf{v} \times \mathbf{B}) + \eta \nabla^2 \mathbf{B}
   \]
   - \(\eta\): Magnetic diffusivity

3. **Ohm’s Law in MHD**:
   \[
   \mathbf{E} + \mathbf{v} \times \mathbf{B} = \eta \mathbf{J}
   \]

4. **Continuity Equation for Mass**:
   \[
   \frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf{v}) = 0
   \]

5. **Gauss's Law for Magnetism**:
   \[
   \nabla \cdot \mathbf{B} = 0
   \]

6. **Magnetization (Magnons)**:
   \[
   \mathbf{M} = \chi \mathbf{H}
   \]
   - \(\mathbf{M}\): Magnetization, \(\chi\): Magnetic susceptibility, \(\mathbf{H}\): Magnetic field intensity

---

## Electric Dynamics Equations (EHD)
1. **Navier-Stokes with Electric Body Force**:
   \[
   \rho \left( \frac{\partial \mathbf{v}}{\partial t} + (\mathbf{v} \cdot \nabla) \mathbf{v} \right) = -\nabla p + \eta \nabla^2 \mathbf{v} + \rho_e \mathbf{E}
   \]
   - \(\rho_e\): Electric charge density

2. **Poisson’s Equation (Electric Potential)**:
   \[
   \nabla^2 \phi = -\frac{\rho_e}{\epsilon}
   \]
   - \(\phi\): Electric potential, \(\epsilon\): Permittivity

3. **Electric Field from Potential**:
   \[
   \mathbf{E} = -\nabla \phi
   \]

4. **Continuity Equation for Electric Charge**:
   \[
   \frac{\partial \rho_e}{\partial t} + \nabla \cdot (\rho_e \mathbf{v}) = -\nabla \cdot \mathbf{J}
   \]

5. **Current Density**:
   \[
   \mathbf{J} = \sigma \mathbf{E} + \rho_e \mathbf{v} + \mathbf{J}_d
   \]
   - \(\sigma\): Conductivity, \(\mathbf{J}_d\): Diffusion current

6. **Electric Body Force Density**:
   \[
   \mathbf{f}_e = \rho_e \mathbf{E} + \frac{1}{2} \mathbf{P} \cdot \nabla \mathbf{E}
   \]

---

## Sonic Dynamics Equations (Phonons)
1. **Wave Equation (Sound Waves)**:
   \[
   \frac{\partial^2 p}{\partial t^2} = c^2 \nabla^2 p
   \]
   - \(p\): Pressure variation, \(c\): Speed of sound

2. **Phonon Energy**:
   \[
   E = \hbar \omega
   \]
   - \(\hbar\): Reduced Planck constant, \(\omega\): Angular frequency

3. **Phonon Dispersion Relation**:
   \[
   \omega = c_s k
   \]
   - \(c_s\): Speed of sound in the material, \(k\): Wave vector

4. **Debye Temperature** (for phonon behavior at low temperatures):
   \[
   \theta_D = \frac{\hbar c_s}{k_B} \left( \frac{6 \pi^2 N}{V} \right)^{1/3}
   \]
   - \(k_B\): Boltzmann constant, \(N\): Number of atoms, \(V\): Volume

5. **Continuity Equation for Phonons**:
   \[
   \frac{\partial n}{\partial t} + \nabla \cdot (n \mathbf{v}) = 0
   \]
   - \(n\): Phonon density

---

## Summary of Equations for Electrons
1. **Schrödinger Equation** (for electron wave function):
   \[
   i \hbar \frac{\partial \psi}{\partial t} = -\frac{\hbar^2}{2m} \nabla^2 \psi + V \psi
   \]
   - \(\psi\): Wave function, \(V\): Potential energy

2. **Electron Current Density**:
   \[
   \mathbf{J} = -e n \mathbf{v}
   \]
   - \(e\): Elementary charge, \(n\): Electron density, \(\mathbf{v}\): Velocity

3. **Electron Cyclotron Frequency** (in a magnetic field):
   \[
   \omega_c = \frac{e B}{m}
   \]
   - \(B\): Magnetic field, \(m\): Electron mass

4. **Lorentz Force on Electron**:
   \[
   \mathbf{F} = -e (\mathbf{E} + \mathbf{v} \times \mathbf{B})
   \]

---

This series provides a compact reference for equations across **MHD**, **EHD**, **phonon dynamics**, **magnons**, and **electrons**. Each set offers essential tools for studying complex interactions between fields, particles, and waves in various physics contexts.
