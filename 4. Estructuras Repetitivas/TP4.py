#Ejercicio 1
cont = 0
while cont < 101:
    print (cont)
    cont = cont + 1 

#Ejercicio 2
numero = int(input("Ingrese un numero: "))
if numero < 0:
    numero = -numero
if numero == 0:
    contador = 1
else:
    contador = 0
    while numero > 0:
        numero = numero // 10
        contador = contador + 1
        
print("El número tiene", contador, "dígito/s.")

#Ejercicio 3
numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))
if numero1 > numero2:
    numero1, numero2 = numero2, numero1
cont = 0
for i in range(numero1 + 1, numero2):
    cont = cont + i
print("La suma de los números entre", numero1, "y", numero2, "es:", cont)

#Ejercicio 4
suma = 0
numero = int(input("Ingrese un numero: "))
while numero != 0:
    suma = suma + numero
    numero = int(input("Ingrese otro numero o un 0 para finalizar: "))
print ("La suma da como resultado: ", suma) 

#Ejercicio 5
import random
numero = random.randint(0, 9)
intentos = 1
numerousuario = int(input("Decime un numero aleatorio del 0 al 9: "))
while numero != numerousuario:
    intentos = intentos + 1
    numerousuario = int(input("Decime un numero aleatorio del 0 al 9: "))
    intentoacertado = intentos + 1
print ("Adivinaste! El numero era el ", numero)
print ("Lo adivinaste en el intento", intentos)

#Ejercicio 6
for i in range(100, -1, -2):
    print(i)

#Ejercicio 7
numero = int(input("Ingrese un numero positivo: "))
suma = 0
for i in range(0, numero + 1):
    suma = suma + i
print("La suma de los números entre 0 y", numero, "es:", suma)

#Ejercicio 8
numero = int(input("Ingrese un numero: "))
pares = 0
impares = 0
positivos = 0
negativos = 0
for i in range (100):
    numero = int(input("Ingrese un numero: "))

    if numero % 2:
        pares = pares + 1
    else:
     impares = impares + 1

    if numero > 0:
        positivos = positivos + 1
    elif numero < 0:
        negativos = negativos + 1

print("Ingresaste", pares, "numeros pares")
print("Ingresaste", impares, "numeros impares")
print("Ingresaste", positivos, "numeros positivos")
print("Ingresaste", negativos, "numeros negativos")

#Ejercicio 9
cantidad = 100
suma = 0
for i in range (100):
    numero = int(input("Ingrese un numero: "))
    suma = suma + numero 
media = suma / cantidad
print ("La media de los numeros ingresados es: ", media)

#Ejercicio 10
numero = int(input("Ingrese un numero: "))
invertido = 0
while numero > 0:
    digito = numero % 10             
    invertido = invertido * 10 + digito  
    numero = numero // 10             
print("El numero invertido es : ", invertido)