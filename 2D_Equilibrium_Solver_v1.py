import numpy as np

#Grid and parameters
Nx,Ny = 100,100 #Grid size
Lx,Ly = 1,1 #single block size
dx,dy = Lx/Nx,Ly/Ny # x axis displacement and y axis displacement

#Initial variables
psi = np.zeros((Nx,Ny)) # initialising the  poloidal flux function on the computational grid.
pressure = lambda psi: 1 - psi**2 # defining pressure function
F = lambda psi: psi # Toroidal flux function

def Laplacian(psi,dx,dy):
    d2x=(np.roll(psi, -1, axis=0) - 2 * psi + np.roll(psi, 1, axis=0)) / dx**2
    d2y=(np.roll(psi, -1, axis=1) - 2 * psi + np.roll(psi, 1, axis=1)) / dy**2
    return d2x + d2y


# Iterative solver
tolerance = 1e-6
for iteration in range(10000000):
    lap_psi = Laplacian(psi, dx, dy)
    dp_dpsi = -2 * psi  # Derivative of pressure
    dF_dpsi = 1  # Derivative of F
    rhs = -dx**2 * (dp_dpsi + dF_dpsi**2 / (1 + psi**2))
    
    # Update psi using relaxation
    psi_new = psi + 0.1 * (lap_psi + rhs)
    
    # Check for convergence
    #if np.max(np.abs(psi_new - psi)) < tolerance:
     #   break
    psi = psi_new

import matplotlib.pyplot as plt
plt.contourf(psi, levels=50)
plt.colorbar()
plt.title("2D Poloidal Flux Contours")
plt.show()
