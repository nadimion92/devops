# -*- coding: utf-8 -*-
"""
@author:Nadime
"""

class Numeros:

    def __init__(self, n):
        self.n = n
        
    def print_numeros(self):
        for number in range(self.n):
            if ((self.n % 2) == 0):
                print("El numero es: ", number)
            else:
                print("El cuadrado del numero es: ", pow(number, 2))
        
        
class Racionales(Numeros):
    
    def __init__(self, n):
        super().__init__(n)
        
    def print_numeros(self):
        print("El número racional es:", self.n)
        print("El número racional en fracción es:", self.n.as_integer_ratio())
    
    def print_hello(self):
        return "Hola soy Nadime"
                
