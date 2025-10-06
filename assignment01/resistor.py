# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 23:29:05 2025

@author: thuri
"""

class Resistor:
    def __init__(self,resistance):
        self.resistance = resistance
        
    def __str__(self):
        return f"{self.resistance}"   
    
    def series(self,other):
        return self.resistance+ other.resistance
    
    def parallel(self,other):
        return (self.resistance*other.resistance)/(self.resistance+other.resistance)
    
R1=Resistor(20)
R2=Resistor(5)

series_result=R1.series(R2)
parallel_result=R1.parallel(R2)

print("Series:",series_result)
print("Parallel:",parallel_result)
