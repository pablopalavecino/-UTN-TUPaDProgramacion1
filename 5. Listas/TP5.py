#Ejercicio1
lista_notas = []
for i in range (10):
    nota = float(input("Ingrese las notas: "))
    lista_notas.append(nota)
print (lista_notas)

suma = 0
for i in lista_notas:
    suma = suma + nota
    promedio = suma / len(lista_notas)
print (promedio)

mayor = lista_notas[0]
menor = lista_notas[0]

for nota in lista_notas:
    if nota > mayor:
        mayor = nota
    if nota < menor:
        menor = nota

print("La nota más alta es:", mayor)
print("La nota más baja es:", menor)

#Ejercicio 2
lista_productos = []
for i in range (5):
    producto = str(input("Ingrese los productos: "))
    lista_productos.append(producto)
ordenados = sorted(lista_productos)
print (ordenados)

eliminar = (input("Que producto desea eliminar  de la lista: "))
if eliminar in ordenados:
    ordenados.remove(eliminar)
    print(f"\nEl producto '{eliminar}' fue eliminado.")
else:
    print(f"\nEl producto '{eliminar}' no está en la lista.")
    
print("Lista actualizada:", ordenados)

#Ejercicio 3
import random
lista_numeros = []
for i in range (15):
    lista_numeros.append(random.randint(1, 100))
print ("La lista de numeros es", lista_numeros)

pares = []
for numero in (lista_numeros):
    if numero % 2 == 0:
        pares.append(numero)
print ("La lista de numeros pares es: ", pares)

impares = []
for numero in (lista_numeros):
    if numero % 2 == 1:
        impares.append(numero)
print ("La lista de numeros impares es: ", impares)

#Ejercicio 4
lista_datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
print ("La lista original es: ", lista_datos)

lista_sinrepetidos = []
for numero in lista_datos:
    if numero not in lista_sinrepetidos:
        lista_sinrepetidos.append(numero)
print ("La lista sin los numeros repetidos es: ", lista_sinrepetidos)

#Ejercicio 5
lista_estudiantes = []
for i in range (8):
    estudiante = str(input("Ingrese los estudiantes: "))
    lista_estudiantes.append(estudiante)
print ("La lista de los estudiantes es: ", lista_estudiantes)

eliminar = (input("Que estudiante desea eliminar  de la lista: "))
if eliminar in lista_estudiantes:
    lista_estudiantes.remove(eliminar)
    print(f"\nEl estudiante '{eliminar}' fue eliminado.")
else:
    print(f"\nEl estudiante '{eliminar}' no está en la lista.")
    
print("Lista actualizada:", lista_estudiantes)

agregar  = (input("Que estudiante decide agregar a la lista?: "))
while agregar in lista_estudiantes:
    print(f"\nEl estudiante '{agregar}' ya está en la lista. Intente con otro nombre.")
    agregar = input("¿Qué estudiante desea agregar a la lista?: ")
lista_estudiantes.append(agregar)
print(f"\nEl estudiante '{agregar}' fue agregado.")
print("Lista actualizada:", lista_estudiantes)

#Ejercicio 6
lista = [1, 2, 3, 4, 5, 6, 7]

print("la ista original:")
for elemento in lista:
    print(elemento, end=" ")
print()

ultimo = lista[-1]

for i in range(len(lista) - 1, 0, -1):
    lista[i] = lista[i - 1]

lista[0] = ultimo

print("la lista despues de rotar hacia la derecha:")
for elemento in lista:
    print(elemento, end=" ")

#Ejercicio 7

temperaturas = [
    [12, 22],  # Día 1
    [15, 25],  # Día 2
    [10, 20],  # Día 3
    [14, 30],  # Día 4
    [18, 28],  # Día 5
    [13, 27],  # Día 6
    [16, 26]   # Día 7
]

print("temperaturas de la semana (mínima, máxima):")
for dia in range(len(temperaturas)):
    print(f"Día {dia+1}: {temperaturas[dia]}")

suma_min = 0
suma_max = 0
for dia in temperaturas:
    suma_min += dia[0]
    suma_max += dia[1]

promedio_min = suma_min / len(temperaturas)
promedio_max = suma_max / len(temperaturas)

print("\npromedio de minimas:", promedio_min)
print("promedio de maximas:", promedio_max)

mayor_amplitud = 0
dia_mayor = 0
for i in range(len(temperaturas)):
    amplitud = temperaturas[i][1] - temperaturas[i][0]
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor = i + 1 

print("\nla mayor amplitud termica fue de", mayor_amplitud, "grados")
print("y fue el dia", dia_mayor)

#Ejercicio 8
notas = [
    [7, 8, 6],
    [5, 6, 7],
    [9, 8, 10],
    [4, 5, 6],
    [10, 9, 8]
]

for i in range(len(notas)):
    prom = sum(notas[i]) / len(notas[i])
    print(f"Promedio estudiante {i+1}: {prom}")

for j in range(3):
    suma = 0
    for i in range(len(notas)):
        suma += notas[i][j]
    print(f"Promedio materia {j+1}: {suma/len(notas)}")


#Ejercicio 9
tablero = [["-"]*3 for _ in range(3)]

def mostrar_tablero(tab):
    for fila in tab:
        for casilla in fila:
            print(casilla, end=" ")
        print()

mostrar_tablero(tablero)

for turno in range(5):  
    jugador = "X" if turno % 2 == 0 else "O"
    fila = int(input(f"\njugador {jugador}, ingrese fila (0-2): "))
    col = int(input("ingrese columna (0-2): "))
    if tablero[fila][col] == "-":
        tablero[fila][col] = jugador
    else:
        print("casilla ocupada, perdiste el turno.")

    mostrar_tablero(tablero)


#Ejercicio 10
ventas = [
    [10, 12, 8, 15, 20, 18, 14],
    [5, 8, 7, 6, 10, 12, 9],
    [20, 22, 25, 18, 19, 21, 23],
    [7, 6, 5, 8, 9, 10, 11]
]

for i in range(len(ventas)):
    total = sum(ventas[i])
    print(f"producto {i+1} total vendido: {total}")

ventas_dias = [0]*7
for j in range(7):
    for i in range(4):
        ventas_dias[j] += ventas[i][j]

dia_max = ventas_dias.index(max(ventas_dias)) + 1
print("dia con mayores ventas:", dia_max)

totales = [sum(prod) for prod in ventas]
prod_max = totales.index(max(totales)) + 1
print("el producto mas vendido:", prod_max)