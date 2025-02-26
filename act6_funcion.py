def print_numbers():
    for number in range(n):
        if ((number % 2) == 0):
            print ("El numero ingfresaado es: ", number)
        else:
            print("El cuadrado del numero es: ", number ** 2)

   
print("Hola Nadime, Ingrese un numero entero")
try:
    n = int(input())
    print("El numero ingresado es ", n)
    print_numbers()

except:
    print("La entrada no es un numero entero")

