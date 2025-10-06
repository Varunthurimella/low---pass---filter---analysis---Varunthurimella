# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 15:42:19 2025

@author: thuri
"""

import math

# Take radius input from user
radius = float(input("Enter the radius of the circle: "))

# Calculate area and circumference
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

# Print results rounded to 2 decimal places
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")


