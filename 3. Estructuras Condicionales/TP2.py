#Ejercicio 1
edad = int (input ("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")
elif edad < 18:
    print("Es menor de edad")

#Ejercicio 2
nota = float(input("Ingrese su nota: "))
if nota > 6:
    print ("Aprobado")
elif nota < 6:
    print ("Desaprobado")

#Ejercicio 3
numero = int(input("Ingrese un numero: "))
if numero % 2 == 0:
    print ("Ha ingresado un número par")
else:
    print ("Por favor, ingrese un número par")

#Ejercicio 4
edad = int(input("Ingrese su edad: "))
if edad >= 0 and edad <= 12:
    print("Pertenece a la categoria Niño/a")
elif edad >= 12 and edad <= 18:
    print ("Pertenece a la categoria Adolescente")
elif edad >= 18 and edad <= 30:
    print ("Pertenece a la categoria Adulto/a Joven")
elif edad >= 30:
    print ("Pertenece a la categoria Adulto")


#Ejercicio 5
contraseña = str(input("Ingrese su contraseña: "))
if len(contraseña) >= 8 and len(contraseña) <= 12:
    print("Ha ingresado una contraseña correcta")
else:
    print ("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6
import random
from statistics import mean, median, mode

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)     
mediana = median(numeros_aleatorios) 
moda = mode(numeros_aleatorios)

print("Lista:", numeros_aleatorios)
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

if media > mediana > moda:
    print("La distribución tiene sesgo positivo a la derecha")
elif media < mediana < moda:
    print("La distribución tiene sesgo negativo a la izquierda")
elif media == mediana == moda:
    print("La distribución no tiene sesgo")
else:
    print("La distribución no cumple con las condiciones de sesgo")

#Ejercicio 7

frase = input("Ingrese una frase: ")
if frase [-1].lower() in "aeiou" :
    frase = frase + "!"
print (frase)

#Ejercicio 8
nombre = str(input("Ingrese su nombre: "))
print("1. Si quiere su nombre en mayúsculas")
print("2. Si quiere su nombre en minúsculas")  
print("3. Si quiere su nombre con la primera letra mayúscula")
opcion = int(input("Ingrese la opcion que desee: "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())

 #Ejercicio 9
magnitud = float(input("Ingrese la magnitud del terremoto segun la escala Richter: "))
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud < 5:
    print ("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud < 6:
    print ("Fuerte (puede causar daños en estructurasdébiles)")
elif magnitud < 7:
    print ("Muy Fuerte (puede causar daños significativos)")
elif magnitud >= 7:
    print ("Extremo (puede causar graves daños a gran escala)")
else:
    print("Ingrese un valor correcto")

#Ejercicio 10
hemisferio = input("Ingrese su hemisferio (N (Norte) / S (Sur)): ").upper()
mes = int(input("Ingrese en que mes del año se encuentra (1-12): "))
dia = int(input("Ingrese que dia es (1-31): "))

if hemisferio == "N": 
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        print ("Te encuentras en Invierno")
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        print ("Te encuentras en Primavera")
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        print ("Te encuentras en Verano")
    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        print ("Te encuentras en Otoño")

if hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        print ("Te encuentras en Verano")
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        print ("Te encuentras en Otoño")
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        print ("Te encuentras en Invierno")
    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        print ("Te encuentras en Primavera")

else:
    print("Por favor, ingrese valores correctos")