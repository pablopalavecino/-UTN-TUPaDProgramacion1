#Ejercicio 1
print ("Hola mundo")

#Ejercicio 2
nombre = input ("Ingrese su nombre: ")
print (f"Hola {nombre}!")

#Ejercicio 3
print ("Ingrese los siguientes datos: ")
nombre = input ("Ingrese su nombre: ")
apellido = input ("Ingrese su apellido: ")
edad = input ("Ingrese su edad: ")
residencia = input ("Ingrese su lugar de residencia: ")
print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Ejercicio 4
pi = 3.14
radio = float (input("Ingrese el radio de un circulo: "))
area = pi * (radio ** 2)
perimetro = 2 * pi * radio
print (f"El area del circulo es {area}")
print (f"el perimetro del circulo es {perimetro}")

#Ejercicio 5
segundos = float (input ("Ingrese la cantidad de segundos: "))
horas = segundos / 3600
print (f"Equivale a {horas} horas")

#Ejercicio 6
numero = int (input("Ingrese un numero: "))
print(numero, "x 1 =", numero * 1)
print(numero, "x 2 =", numero * 2)
print(numero, "x 3 =", numero * 3)
print(numero, "x 4 =", numero * 4)
print(numero, "x 5 =", numero * 5)
print(numero, "x 6 =", numero * 6)
print(numero, "x 7 =", numero * 7)
print(numero, "x 8 =", numero * 8)
print(numero, "x 9 =", numero * 9)
print(numero, "x 10 =", numero * 10)

#Ejercicio 7
n1 = int(input("Ingrese el primer numero, que sea diferente de 0: "))
n2 = int(input("Ingrese el segundo numero, que sea diferente de 0: "))
print (f"Suma: {n1 + n2}")
print (f"Resta: {n1 - n2}")
print (f"Multiplicacion: {n1 * n2}")
print (f"Division: {n1 / n2}")

#Ejercicio 8
altura = float(input ("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilos: "))
print (f"Su masa corporal es: {peso / (altura**2)}")

#Ejercicio 9
celsius = float(input ("Ingrese la temperatura en grados celsius: "))
fahrenheit = (9/5) * celsius + 32
print (f"La temperatura de {celsius} grados Celsius, equivale a {fahrenheit} grados Fahrenheit")

#Ejercicio 10
n1 = int(input ("Ingrese el primer numero: "))
n2 = int(input ("Ingrese el segundo numero: "))
n3 = int(input ("Ingrese el tercer numero: "))
promedio = (n1 + n2 + n3) / 3
print (f"El promedio de los 3 numeros es {promedio}")