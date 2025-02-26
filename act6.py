print("Hola Nadime, Ingrese un numero entero")

try: 
    n = int(input())
    print("El numero ingresado es ", n)

    for number in range(n):
        if ((number % 2) == 0):
            print("residuo es: " , number % 2)
            print("EL numero es: ", number)
        else:
            print("El cuadrado del numero es: ", pow(number,2))
except:
    print("La entrada no es un numero entero")
