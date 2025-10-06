# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 22:37:36 2025

@author: thuri
"""

import matplotlib.pyplot as plt

R = 10  

print("Voltage (V)   Current (A)")
print("-" * 25)

voltages = range(1, 13)  
currents = []  

for V in voltages:
    I = V / R  
    currents.append(I)
    print(f"{V:<12} {I:.2f}")


plt.plot((voltages), currents, marker='o')
plt.title("IV Characteristics (R = 10Ω)")
plt.xlabel("Voltage (V)")
plt.ylabel("Current (A)")
plt.grid(True)
plt.show()




