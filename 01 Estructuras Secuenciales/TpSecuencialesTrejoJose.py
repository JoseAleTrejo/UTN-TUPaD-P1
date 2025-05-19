import time
# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print ("Hola mundo!")

time.sleep(2)

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario 
# ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
# la impresión por pantalla.

nombre = input("Ingrese el nombre: ")
print (f"Hola {nombre}")

time.sleep(2)

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos 
# ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 
# 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla. 1

nombre = input ("Ingrese su nombre: ")
apellido = input ("Ingrese su apellido: ")
edad = input ("Ingrese su edad: ")
residencia = input ("Ingrese su residencia:")

print (f"Soy {nombre} {apellido}, tengo {edad} y vivo en {residencia}")

time.sleep(2)

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

radio = float(input ("Ingrese el radio: "))
perimetro = 2 * radio * 3.1416
area = radio ** 2 * 3.1416
print (f"El area es {area} y el perimetro es {perimetro}")

time.sleep(2)

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

segundos  = int(input("Ingrese la cantidad de segundos:"))
minutos = segundos / 60
horas = minutos / 60
print (f"Equivale a {horas}")

time.sleep(2)

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

numero = int(input("Ingrese un numero entero: "))

for i in range(10):
    print (f"{i} * {numero} = ", i * numero)

time.sleep(2)

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, 
# multiplicarlos y restarlos.

numero1 = int(input("Ingrese un numero entero mayor que cero: "))
numero2 = int(input("ingrese otro numero entero mayor que cero: "))

suma = numero1 + numero2
resta = numero1 - numero2
producto = numero1 * numero2
cociente = numero1 / numero2

print(f"Las operaciones entre {numero1} y {numero2} fueron SUMA:",suma," RESTA: ",resta, " PRODUCTO:",producto," COCIENTE:",cociente)

time.sleep(2)

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que el índice 
# de masa corporal se calcula del siguiente modo:

altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))
imc = peso / altura ** 2

print ("El indice de masa corporal es: " ,imc)

time.sleep(2)

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. 
# Tener en cuenta la siguiente equivalencia:

celsius = float(input("Ingrese la temperatura en celsius: "))
farenheit = 9/5 * celsius + 32

print(f"El equivalente de {celsius} grados celsius es :",farenheit," grados farenheit")

time.sleep(2)

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

numero1 = int(input("Ingrese el primer numero:"))
numero2 = int(input("Ingrese el segundo numero:"))
numero3 = int(input("Ingrese el tercer numero:"))

promedio = ((numero1 + numero2 + numero3)/3)

print("El promedio es: ", promedio)

print ("FIN DE LA PRACTICA DE SECUENCIALES")