import numpy as np
import matplotlib.pyplot as plt

# Grid and parameters
Nx, Ny = 100, 100  # Grid size
Lx, Ly = 1, 1      # Domain size
dx, dy = Lx / Nx, Ly / Ny  # Grid spacing

# Initial variables
psi = np.zeros((Nx, Ny))  # Initial poloidal flux function
pressure = lambda psi: 1 - psi**2  # Pressure function
F = lambda psi: psi  # Toroidal flux function

def Laplacian(psi, dx, dy):
    """Compute the Laplacian of psi using finite differences."""
    d2x = (np.roll(psi, -1, axis=0) - 2 * psi + np.roll(psi, 1, axis=0)) / dx**2
    d2y = (np.roll(psi, -1, axis=1) - 2 * psi + np.roll(psi, 1, axis=1)) / dy**2
    return d2x + d2y

# Iterative solver
tolerance = 1e-6
omega = 0.1  # Relaxation factor
for iteration in range(100000):
    # Compute Laplacian
    lap_psi = Laplacian(psi, dx, dy)
    # Compute derivatives of pressure and current
    dp_dpsi = -2 * psi  # Derivative of pressure
    dF_dpsi = 1  # Derivative of F
    # Right-hand side
    rhs = -dp_dpsi - F(psi) * dF_dpsi
    # Update psi using relaxation
    psi_new = psi + omega * (lap_psi + rhs)
    # Apply boundary conditions
    psi_new[0, :] = 0  # Top boundary
    psi_new[-1, :] = 0  # Bottom boundary
    psi_new[:, 0] = 0  # Left boundary
    psi_new[:, -1] = 0  # Right boundary
    # Check for convergence
    residual = np.max(np.abs(psi_new - psi))
    if iteration % 1000 == 0:
        print(f"Iteration {iteration}, Residual: {residual}")
    if residual < tolerance:
        print(f"Converged after {iteration} iterations.")
        break
    psi = psi_new

# Plot results
plt.contourf(psi, levels=50, cmap="viridis")
plt.colorbar()
plt.title("2D Poloidal Flux Contours")
plt.show()

