# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 15:58:09 2025

@author: thuri
"""

numbers = list(range(1,11))

squares=[]

for num in numbers:
    squares.append(num**2)
    
    sum_of_squares = sum(squares)
    
    
print("Squares:",squares)
print("Sum of Squares:",sum_of_squares)