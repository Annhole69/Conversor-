
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("conversor de temperatura")
print("1. Celsius a Fahrenheit")
print("2. Fahrenheit a Celsius")

opcion = input("Elige una opcion (1 o 2):")

if opcion == "1":
    celsius = float(input("Ingresa la temperatura en Celsius:  "))
    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"{celsius}C es igual a {fahrenheit}F" )     
elif opcion == "2":
    fahrenheit = float(input("Ingresa la temperatura en Fahrenheit: "))
    celsius = fahrenheit_a_celsius(fahrenheit)
    print = (f"{fahrenheit}F es igual a {celsius}C")
else: 
    print("Esta opción no es valida")    