# Fundamental Constants and Units for MHD, EHD, and Phonon Dynamics

This document provides a reference for fundamental constants, units, and conversion tips relevant to **Magnetohydrodynamics (MHD)**, **Electrohydrodynamics (EHD)**, and **Phonon Dynamics**. These constants are critical for calculations and modeling in these fields, and understanding the unit systems can help ensure accuracy across different scientific contexts.

---

## Key Constants

| Constant                         | Symbol      | Value                        | Units (SI)            | Description                                     |
|----------------------------------|-------------|------------------------------|------------------------|-------------------------------------------------|
| **Permittivity of Free Space**   | $\epsilon_0$ | $8.854 \times 10^{-12}$      | F/m (farads per meter) | Governs electric field strength in a vacuum     |
| **Permeability of Free Space**   | $\mu_0$     | $4\pi \times 10^{-7}$        | H/m (henries per meter) | Governs magnetic field strength in a vacuum     |
| **Elementary Charge**            | $e$         | $1.602 \times 10^{-19}$      | C (coulombs)          | Charge of a single proton                       |
| **Planck's Constant**            | $h$         | $6.626 \times 10^{-34}$      | J·s (joule-seconds)   | Relates energy and frequency in quantum systems |
| **Reduced Planck's Constant**    | $\hbar$     | $1.055 \times 10^{-34}$      | J·s (joule-seconds)   | $\hbar = h / (2\pi)$, used in wave dynamics     |
| **Boltzmann Constant**           | $k_B$       | $1.381 \times 10^{-23}$      | J/K (joules per kelvin)| Relates temperature and energy                  |
| **Speed of Light in Vacuum**     | $c$         | $3.00 \times 10^8$           | m/s (meters per second) | Speed of light, critical in EHD and MHD theories|
| **Electron Mass**                | $m_e$       | $9.109 \times 10^{-31}$      | kg (kilograms)        | Mass of an electron, relevant for charge dynamics|
| **Proton Mass**                  | $m_p$       | $1.673 \times 10^{-27}$      | kg (kilograms)        | Mass of a proton                                |
| **Avogadro's Number**            | $N_A$       | $6.022 \times 10^{23}$       | 1/mol                 | Number of particles per mole                    |

---

## Commonly Used Units

### SI Units

The **International System of Units (SI)** is widely used for scientific calculations in MHD, EHD, and phonon dynamics. Here’s a summary of commonly used SI units in these fields:

| Quantity                  | SI Unit       | Symbol     |
|---------------------------|---------------|------------|
| **Electric Field**        | volts per meter | V/m       |
| **Magnetic Field**        | tesla          | T         |
| **Charge**                | coulomb        | C         |
| **Current**               | ampere         | A         |
| **Potential Difference**  | volt           | V         |
| **Capacitance**           | farad          | F         |
| **Inductance**            | henry          | H         |
| **Frequency**             | hertz          | Hz        |
| **Energy**                | joule          | J         |
| **Force**                 | newton         | N         |
| **Length**                | meter          | m         |
| **Mass**                  | kilogram       | kg        |
| **Time**                  | second         | s         |

### CGS Units

The **Centimeter-Gram-Second (CGS)** unit system is still used in some areas of physics, particularly in electromagnetic theory. Below are some CGS units relevant to EHD and MHD:

| Quantity                  | CGS Unit           | Symbol     |
|---------------------------|--------------------|------------|
| **Electric Field**        | statvolt/cm       | statV/cm   |
| **Magnetic Field**        | gauss             | G          |
| **Charge**                | statcoulomb       | statC      |
| **Potential Difference**  | statvolt          | statV      |
| **Energy**                | erg               | erg        |
| **Force**                 | dyne              | dyn        |
| **Length**                | centimeter        | cm         |
| **Mass**                  | gram              | g          |
| **Time**                  | second            | s          |

---

## Conversion Tips: SI vs. CGS Units

| Quantity                  | SI to CGS Conversion                             | CGS to SI Conversion                             |
|---------------------------|--------------------------------------------------|--------------------------------------------------|
| **Electric Field**        | $1\ \mathrm{V/m} = 10^6\ \mathrm{statV/cm}$     | $1\ \mathrm{statV/cm} = 10^{-6}\ \mathrm{V/m}$  |
| **Magnetic Field**        | $1\ \mathrm{T} = 10^4\ \mathrm{G}$              | $1\ \mathrm{G} = 10^{-4}\ \mathrm{T}$           |
| **Charge**                | $1\ \mathrm{C} = 3 \times 10^9\ \mathrm{statC}$ | $1\ \mathrm{statC} = 3.33 \times 10^{-10}\ \mathrm{C}$ |
| **Energy**                | $1\ \mathrm{J} = 10^7\ \mathrm{erg}$            | $1\ \mathrm{erg} = 10^{-7}\ \mathrm{J}$         |
| **Force**                 | $1\ \mathrm{N} = 10^5\ \mathrm{dyn}$            | $1\ \mathrm{dyn} = 10^{-5}\ \mathrm{N}$         |
| **Length**                | $1\ \mathrm{m} = 100\ \mathrm{cm}$              | $1\ \mathrm{cm} = 0.01\ \mathrm{m}$             |
| **Mass**                  | $1\ \mathrm{kg} = 10^3\ \mathrm{g}$             | $1\ \mathrm{g} = 10^{-3}\ \mathrm{kg}$          |

### Quick Conversion Tips
- **Magnetic Field**: Convert tesla to gauss by multiplying by \(10^4\).
- **Electric Field**: Convert volts per meter to statvolts per centimeter by multiplying by \(10^6\).
- **Energy**: Joules are significantly larger than ergs, with \(1\ \mathrm{J} = 10^7\ \mathrm{erg}\).

---

## Quick Reference for Constants and Units in Phonon Dynamics

In **phonon dynamics**, constants and units related to wave behavior and thermal interactions are frequently used:

- **Wave Vector ($k$)**: SI unit is 1/m (meters inverse); describes the spatial frequency of a wave.
- **Angular Frequency ($\omega$)**: Measured in radians per second (rad/s), related to the oscillation rate of phonons.
- **Debye Temperature ($\theta_D$)**: Unit is Kelvin (K); indicates the temperature above which phonons contribute significantly to specific heat.
- **Planck’s Reduced Constant ($\hbar$)**: Unit is J·s; critical in quantizing phonon energy as \( E = \hbar \omega \).

---

## Summary

This document provides a quick reference to the fundamental constants and units used across MHD, EHD, and phonon dynamics. Knowing these constants and their conversions is essential for accurate calculations in these fields. Understanding the difference between SI and CGS systems will also help you interpret and compare research from different scientific disciplines.

For more on the equations involving these constants, refer to the [Magnetic, Electric, and Sonic Dynamics Equations](Magnetic_Electric_Sonic_Dynamics_Equations.md) document.
