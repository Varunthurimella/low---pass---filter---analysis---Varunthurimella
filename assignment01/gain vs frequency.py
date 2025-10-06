# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 00:52:29 2025

@author: thuri
"""

import matplotlib.pyplot as plt
import math

data = [
        (100, 1.00, 0.99),
        (500, 1.00, 0.95),
        (1000, 1.00, 0.85),
        (2000, 1.00, 0.62),
        (5000, 1.00, 0.30),
        (10000, 1.00, 0.16), 
        ]
frequencies = []
gain_db = []
for f,vin,vout in data:
     gain = vout/vin
     gdb = 20*math.log10(gain)
     frequencies.append(f)
     gain_db.append(gdb)
     
plt.figure(figsize=(8,5))
plt.semilogx(frequencies, gain_db,marker='o',linestyle='-',color='b') 
plt.grid(True,which="both",linestyle="--",linewidth=0.7)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Gain(dB)")
plt.title("Gain (dB) vs Frequency for RC Filter")
plt.tight_layout()
plt.show()    