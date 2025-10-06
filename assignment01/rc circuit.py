# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 22:36:58 2025

@author: thuri
"""

import numpy as np
import matplotlib.pyplot as plt

Vmax = 5       
R= 1000   
C = 100e-6     


tau = R * C
print(f"Time constant (τ): {tau:.4f} seconds")

t = np.linspace(0, 1, 1000)

V_t = Vmax * (1 - np.exp(-t / tau))

V_tau = 0.63 * Vmax


plt.plot(t, V_t, label="V(t) = Charging Curve")
plt.axhline(V_tau, color='red', linestyle='--', label="63% of Vmax")
plt.axvline(tau, color='green', linestyle='--', label="τ (time constant)")
plt.scatter(tau, V_tau, color='black', zorder=5)

plt.title("RC Circuit Charging Curve")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.grid(True)
plt.legend()
plt.show()
