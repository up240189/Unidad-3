'''
1. Filter only negative and zero in the list using list comprehension
2. Flatten the following list of lists of lists to a one dimensional list :
3. Using list comprehension create the following list of tuples:
4. Flatten the following list to a new list:
5. Change the following list to a list of dictionaries:
6. Change the following list of lists to a list of concatenated strings:
7. Write a lambda function which can solve a slope or y-intercept of linear functions.
'''

numeros = [-4, -3, -2, -1, 0, 2, 4, 6]
negativos_y_cero = [num for num in numeros if num <= 0]
print("Negativos y cero:", negativos_y_cero)

listas_de_listas = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
lista_aplanada = [numero for sublista in listas_de_listas for lista in sublista for numero in lista]
print("Lista aplanada:", lista_aplanada)

tuplas = [(x, 1, x, x**2, x**3, x**4, x**5) for x in range(11)]
print("Tuplas:", tuplas)

paises = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
paises_formateados = [[pais[0].upper(), pais[0][:3].upper(), pais[1].upper()] for sublista in paises for pais in sublista]
print("Países formateados:", paises_formateados)

paises_diccionarios = [{'country': pais[0].upper(), 'city': pais[1].upper()} for sublista in paises for pais in sublista]
print("Países como diccionarios:", paises_diccionarios)

nombres = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
nombres_concatenados = [' '.join(nombre) for sublista in nombres for nombre in sublista]
print("Nombres concatenados:", nombres_concatenados)

calcular_pendiente = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else None
calcular_interseccion = lambda x, y, pendiente: y - pendiente * x

pendiente = calcular_pendiente(1, 2, 3, 6)
interseccion = calcular_interseccion(1, 2, pendiente)
print(f"Pendiente: {pendiente}, Intersección en y: {interseccion}")