# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 23:44:23 2025

@author: thuri
"""

class ComplexNumber:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
        
    def __str__(self):
        return f"{self.real} + {self.imag}i"
    
    def __add__(self,other):
        return ComplexNumber (self.real+ other.real,self.imag+other.imag)
    
    def __sub__(self,other):
        return ComplexNumber (self.real-other.real,self.imag-other.imag)
    
c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(1, 2)

sum_result = c1 + c2
diff_result = c1 - c2

print("Sum:", sum_result)
print("Difference:", diff_result)