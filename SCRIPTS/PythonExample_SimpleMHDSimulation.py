from fenics import *
import matplotlib.pyplot as plt

# Define mesh and function space
mesh = UnitSquareMesh(32, 32)
V = VectorFunctionSpace(mesh, 'P', 2)

# Define magnetic field parameters
B = Constant((0, 0.1))  # Magnetic field vector in y-direction

# Define boundary conditions (no-slip at boundaries)
u = Function(V)
bc = DirichletBC(V, Constant((0, 0)), 'on_boundary')

# Define MHD problem
rho = Constant(1.0)  # Fluid density
eta = Constant(0.1)  # Dynamic viscosity
f = Constant((0, 0))  # External force

# Weak form
u_trial = TrialFunction(V)
u_test = TestFunction(V)
a = eta * inner(grad(u_trial), grad(u_test)) * dx
L = dot(f, u_test) * dx + dot(cross(B, u), u_test) * dx

# Solve and plot
solve(a == L, u, bc)
plot(u, title='MHD Flow under Magnetic Field')
plt.show()
