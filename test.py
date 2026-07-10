from classy import Class
import numpy as np
import matplotlib.pyplot as plt

# Initialize CLASS
cosmo = Class()

params = {
    # Cosmology
    'h': 0.7,
    'Omega_cdm': 0.99,
    'Omega_b': 0.01,
    'N_ur': 0.0,
    'N_ncdm': 0,

    # Primordial spectrum
    'A_s': 2.1e-9,
    'n_s': 0.965,

    # Request transfer functions
    'output': 'mTk',
    'P_k_max_h/Mpc': 10.0,
    'z_pk': '0'
}

cosmo.set(params)
cosmo.compute()

# Obtain transfer functions
transfers = cosmo.get_transfer(z=0)

k = transfers['k (h/Mpc)']
T_cdm = transfers['d_cdm']

plt.figure(figsize=(7,5))
plt.loglog(k, np.abs(T_cdm))

plt.xlabel(r"$k\,[h/{\rm Mpc}]$")
plt.ylabel(r"$|T(k)|$")
plt.title("CDM Transfer Function")
plt.grid(True, which="both")
plt.show()

cosmo.struct_cleanup()
cosmo.empty()