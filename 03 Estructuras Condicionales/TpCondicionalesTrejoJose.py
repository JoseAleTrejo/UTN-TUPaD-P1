from time import sleep
# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga 
# “Es mayor de edad”.

edad = int(input("Ingrese la edad del usuario: "))

if edad >= 18:
    print("Es mayor de edad!!")

sleep(2)
print("\n") 

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que 
# diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

nota = int(input("Ingrese la nota: "))

if nota >= 6:
    print ("Esta aprobado!")
else:
    print ("Esta desaprobado!")

sleep(2)
print("\n")

# Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el 
# mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar 
# el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

numero = int(input("Ingrese un numero: "))

if numero % 2 == 0:
    print ("Ha ingresado un numero par!")
else:
    print ("Por favor ingrese un numero par!")

sleep(2)
print("\n")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: 
# ● Niño/a: menor de 12 años. 
# ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años. 

edad = int(input("Ingrese su edad:"))

if edad < 12:
    print ("Es un niño/a")
else:
    if edad < 18:
        print ("Es un adolescente")
    else:
        if edad < 30:
            print ("Es un adulto/a joven")
        else:
            print ("Es un adulto mayor:")

sleep(2)
print("\n")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una 
# contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, 
# imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en 
# Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

password = input ("Ingrese la contraseña:")

if len(password) >= 8 and len(password) <= 14:
    print ("Ha ingresado una contraseña correcta!")
else:
    print ("Ingrese una contraseña entre 8 y 14 caracteres!")

sleep(2)
print("\n")

# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números y calcular la moda, la mediana y la 
# media de dichos números
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se pueden utilizar para predecir la forma de una 
# distribución normal a partir del siguiente criterio: 
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su 
# vez, la mediana es mayor que la moda. 
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda. 
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
#Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su 
# media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

from statistics import mode,median,mean
import random

numeros_aleatorios = [random.randint(1,100) for i in range(50)]
print (numeros_aleatorios)

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana and mediana > moda:
    print ("Tiene sesgo positivo!")
else:
    if media < mediana and mediana < moda:
        print ("Tiene sesgo negativo!") 
    else:
        if media == mediana and media == moda and mediana == moda:
            print ("No tiene sesgo!")

sleep(2)
print("\n")

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input("Ingrese su nombre:")
opcion = int(input("Ingrese 1 - Mayusculas "
               "Ingrese 2 - Minusculas " 
               "Ingrese 3 - Primer letra mayuscula:"))

if opcion == 1:
    transformar = nombre.upper()
else:
    if opcion == 2:
        transformar = nombre.lower()
    else:
        transformar = nombre.title()

print (f"{transformar}")

sleep(2)

print("Me faltan algunos ejercicios!")            
               

