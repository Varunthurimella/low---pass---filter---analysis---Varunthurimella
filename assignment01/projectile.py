# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 17:17:44 2025

@author: thuri
"""

import numpy as np
import matplotlib.pyplot as plt

g = 9.81  

u = float(input("Enter initial velocity (m/s): "))
theta_deg = float(input("Enter launch angle (degrees): "))
h0 = 1.0

theta = np.radians(theta_deg)

a = -0.5 * g
b = u * np.sin(theta)
c = h0

discriminant = b**2 - 4*a*c
t_flight = (-b + np.sqrt(discriminant)) / (2*a)  

H = h0 + (u**2) * (np.sin(theta)**2) / (2*g)

R = u * np.cos(theta) * t_flight

t = np.linspace(0, t_flight, 500)

x = u * np.cos(theta) * t
y = h0 + u * np.sin(theta) * t - 0.5 * g * t**2

plt.plot(x, y)
plt.title(f"Projectile Motion (u={u} m/s, θ={theta_deg}°)")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Height (m)")
plt.grid(True)
plt.axhline(0, color='black', linewidth=1.0)  # ground line
plt.show()
print(f"Maximum Height: {H:.2f} m")
print(f"Horizontal Range: {R:.2f} m")


