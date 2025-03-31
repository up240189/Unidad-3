'''
### Exercises: Level 1

1. Iterate 0 to 10 using for loop, do the same using while loop.
2. Iterate 10 to 0 using for loop, do the same using while loop.
3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
4. Use nested loops to create the following:
5. Print the following pattern:
6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
7. Use for loop to iterate from 0 to 100 and print only even numbers
8. Use for loop to iterate from 0 to 100 and print only odd numbers
   
### Exercises: Level 2
    
1.  Use for loop to iterate from 0 to 100 and print the sum of all numbers.
2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

### Exercises: Level 3

1. Go to the data folder and use the [countries.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py) file. Loop through the countries and extract all the countries containing the word _land_.
2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
3. Go to the data folder and use the [countries_data.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file. 
'''

print("Iterar de 0 a 10 usando for:")
for i in range(11):
    print(i)

print("Iterar de 0 a 10 usando while:")
i = 0
while i <= 10:
    print(i)
    i += 1

print("Iterar de 10 a 0 usando for:")
for i in range(10, -1, -1):
    print(i)

print("Iterar de 10 a 0 usando while:")
i = 10
while i >= 0:
    print(i)
    i -= 1

for i in range(1, 8):
    print('#' * i)

for i in range(8):
    print('# ' * 8)

for i in range(11):
    print(f"{i} x {i} = {i * i}")

lista = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for elemento in lista:
    print(elemento)

print("Números pares del 0 al 100:")
for i in range(0, 101, 2):
    print(i)

print("Números impares del 0 al 100:")
for i in range(1, 101, 2):
    print(i)

suma_total = sum(range(101))
print(f"La suma de todos los números es {suma_total}.")

suma_pares = sum(range(0, 101, 2))
suma_impares = sum(range(1, 101, 2))
print(f"La suma de todos los pares es {suma_pares}. Y la suma de todos los impares es {suma_impares}.")

paises = ["Finland", "Switzerland", "Ireland", "Iceland", "Thailand", "Poland", "England"]
paises_con_land = [pais for pais in paises if "land" in pais]
print("Países que contienen 'land':", paises_con_land)

frutas = ['banana', 'orange', 'mango', 'lemon']
frutas_revertidas = []
for fruta in frutas[::-1]:
    frutas_revertidas.append(fruta)
print("Lista de frutas en orden inverso:", frutas_revertidas)
