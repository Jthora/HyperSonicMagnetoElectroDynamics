# Magnetic and Electric and Sonic Dynamics Equations (MHD, EHD, Phonons, Magnons, and Electrons)

---

## Magnetic Dynamics Equations (MHD)

1. **Navier-Stokes with Lorentz Force** (for fluid in magnetic fields):
   - Equation: ρ (∂v/∂t + (v ⋅ ∇) v) = −∇p + η ∇²v + J × B
   - Where:
     - ρ: Fluid density
     - v: Velocity
     - J: Current density
     - B: Magnetic field

2. **Magnetic Induction Equation** (for time evolution of B):
   - Equation: ∂B/∂t = ∇ × (v × B) + η ∇²B
   - Where η is the magnetic diffusivity

3. **Ohm’s Law in MHD**:
   - Equation: E + v × B = η J

4. **Continuity Equation for Mass**:
   - Equation: ∂ρ/∂t + ∇ ⋅ (ρ v) = 0

5. **Gauss's Law for Magnetism**:
   - Equation: ∇ ⋅ B = 0

6. **Magnetization (Magnons)**:
   - Equation: M = χ H
   - Where:
     - M: Magnetization
     - χ: Magnetic susceptibility
     - H: Magnetic field intensity

---

## Electric Dynamics Equations (EHD)

1. **Navier-Stokes with Electric Body Force**:
   - Equation: ρ (∂v/∂t + (v ⋅ ∇) v) = −∇p + η ∇²v + ρ_e E
   - Where ρ_e is the electric charge density

2. **Poisson’s Equation (Electric Potential)**:
   - Equation: ∇²φ = −ρ_e/ε
   - Where:
     - φ: Electric potential
     - ε: Permittivity

3. **Electric Field from Potential**:
   - Equation: E = −∇φ

4. **Continuity Equation for Electric Charge**:
   - Equation: ∂ρ_e/∂t + ∇ ⋅ (ρ_e v) = −∇ ⋅ J

5. **Current Density**:
   - Equation: J = σ E + ρ_e v + J_d
   - Where:
     - σ: Conductivity
     - J_d: Diffusion current

6. **Electric Body Force Density**:
   - Equation: f_e = ρ_e E + ½ P ⋅ ∇E

---

## Sonic Dynamics Equations (Phonons)

1. **Wave Equation (Sound Waves)**:
   - Equation: ∂²p/∂t² = c² ∇²p
   - Where:
     - p: Pressure variation
     - c: Speed of sound

2. **Phonon Energy**:
   - Equation: E = ℏω
   - Where:
     - ℏ: Reduced Planck constant
     - ω: Angular frequency

3. **Phonon Dispersion Relation**:
   - Equation: ω = c_s k
   - Where:
     - c_s: Speed of sound in the material
     - k: Wave vector

4. **Debye Temperature** (for phonon behavior at low temperatures):
   - Equation: θ_D = (ℏ c_s / k_B) (6π² N / V)^(1/3)
   - Where:
     - k_B: Boltzmann constant
     - N: Number of atoms
     - V: Volume

5. **Continuity Equation for Phonons**:
   - Equation: ∂n/∂t + ∇ ⋅ (n v) = 0
   - Where n is the phonon density

---

## Summary of Equations for Electrons

1. **Schrödinger Equation** (for electron wave function):
   - Equation: iℏ ∂ψ/∂t = −(ℏ² / 2m) ∇²ψ + Vψ
   - Where:
     - ψ: Wave function
     - V: Potential energy

2. **Electron Current Density**:
   - Equation: J = −e n v
   - Where:
     - e: Elementary charge
     - n: Electron density
     - v: Velocity

3. **Electron Cyclotron Frequency** (in a magnetic field):
   - Equation: ω_c = e B / m
   - Where:
     - B: Magnetic field
     - m: Electron mass

4. **Lorentz Force on Electron**:
   - Equation: F = −e (E + v × B)

---

This series provides a compact reference for equations across MHD, EHD, phonon dynamics, magnons, and electrons. Each set offers essential tools for studying complex interactions between fields, particles, and waves in various physics contexts.
