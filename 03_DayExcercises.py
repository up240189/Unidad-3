'''
1. Declare your age as integer variable
2. Declare your height as a float variable
3. Declare a variable that store a complex number
4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
9. Slope is (m = y2-y1/x2-x1). Find the slope and [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance#:~:text=In%20mathematics%2C%20the%20Euclidean%20distance,being%20called%20the%20Pythagorean%20distance.) between point (2, 2) and point (6,10) 
10. Compare the slopes in tasks 8 and 9.
11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
13. Use _and_ operator to check if 'on' is found in both 'python' and 'dragon'
14. _I hope this course is not full of jargon_. Use _in_ operator to check if _jargon_ is in the sentence.
15. There is no 'on' in both dragon and python
16. Find the length of the text _python_ and convert the value to float and convert it to string
17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
19. Check if type of '10' is equal to type of 10
20. Check if int('9.8') is equal to 10
21. Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
23. Write a Python script that displays the following table
'''

edad = 25

altura = 5.9

numero_complejo = 2 + 3j

base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))
area = 0.5 * base * altura
print(f"El área del triángulo es {area}")

lado_a = float(input("Ingrese el lado a: "))
lado_b = float(input("Ingrese el lado b: "))
lado_c = float(input("Ingrese el lado c: "))
perimetro = lado_a + lado_b + lado_c
print(f"El perímetro del triángulo es {perimetro}")

longitud = float(input("Ingrese la longitud: "))
anchura = float(input("Ingrese la anchura: "))
area = longitud * anchura
perimetro = 2 * (longitud + anchura)
print(f"El área del rectángulo es {area}")
print(f"El perímetro del rectángulo es {perimetro}")

import math
radio = float(input("Ingrese el radio: "))
area = math.pi * radio * radio
circunferencia = 2 * math.pi * radio
print(f"El área del círculo es {area}")
print(f"La circunferencia del círculo es {circunferencia}")

x1, y1 = 2, 2
x2, y2 = 6, 10
pendiente = (y2 - y1) / (x2 - x1)
distancia_euclidiana = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"Pendiente: {pendiente}")
print(f"Distancia euclidiana: {distancia_euclidiana}")

def calcular_y(x):
    return x ** 2 + 6 * x + 9

valores_x = [-6, -3, 0, 3, 6]
for x in valores_x:
    y = calcular_y(x)
    print(f"Para x = {x}, y = {y}")

# El valor de y es 0 cuando x = -3

longitud_python = len("python")
longitud_dragon = len("dragon")
comparacion_falsa = longitud_python != longitud_dragon
print(f"¿Es la longitud de 'python' diferente a la longitud de 'dragon'? {comparacion_falsa}")

resultado = 'on' in 'python' and 'on' in 'dragon'
print(resultado)

oracion = "I hope this course is not full of jargon"
resultado = 'jargon' in oracion
print(resultado)

resultado = 'on' not in 'dragon' and 'on' not in 'python'
print(resultado)

longitud_python = len("python")
longitud_flotante = float(longitud_python)
longitud_cadena = str(longitud_flotante)
print(longitud_cadena)

numero = int(input("Ingrese un número: "))
es_par = (numero % 2 == 0)
print(f"¿Es el número par? {es_par}")

resultado = (7 // 3 == int(2.7))
print(resultado)

resultado = type('10') == type(10)
print(resultado)

try:
    resultado = int('9.8') == 10
except ValueError:
    resultado = False
print(resultado)

horas = float(input("Ingrese horas: "))
tarifa_por_hora = float(input("Ingrese la tarifa por hora: "))
ganancia_semanal = horas * tarifa_por_hora
print(f"Tu ganancia semanal es {ganancia_semanal}")

anios_vividos = float(input("Ingrese el número de años que ha vivido: "))
segundos_en_un_anio = 365 * 24 * 60 * 60
segundos_vividos = anios_vividos * segundos_en_un_anio
print(f"Has vivido {segundos_vividos} segundos.")

for i in range(1, 6):
    print(f"{i} 1 {i} {i**2} {i**3}")
