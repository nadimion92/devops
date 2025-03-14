# -*- coding: utf-8 -*-
"""
@author: nadime
"""

import act7_1_numeros
import ac7_3_abstrac_class

print("Ingrese un numero: ")
n = int(input())
enteros = act7_1_numeros.Numeros(n)
enteros.print_numeros()

print("Ingresa un numero racional: ")
q = float(input())
racionales = act7_1_numeros.Racionales(q)
racionales.print_numeros()

print("Ingrese un numero para el modulo abstracto:")
m = float(input())
racionales = ac7_3_abstrac_class.Racionales(m)
racionales.print_numeros()

