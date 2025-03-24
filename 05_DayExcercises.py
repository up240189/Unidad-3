'''
1. Declare an empty list
2. Declare a list with more than 5 items
3. Find the length of your list
4. Get the first item, the middle item and the last item of the list
5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
7. Print the list using _print()_
8. Print the number of companies in the list
9. Print the first, middle and last company
10. Print the list after modifying one of the companies
11. Add an IT company to it_companies
12. Insert an IT company in the middle of the companies list
13. Change one of the it_companies names to uppercase (IBM excluded!)
14. Join the it_companies with a string '#;&nbsp; '
15. Check if a certain company exists in the it_companies list.
16. Sort the list using sort() method
17. Reverse the list in descending order using reverse() method
18. Slice out the first 3 companies from the list
19. Slice out the last 3 companies from the list
20. Slice out the middle IT company or companies from the list
21. Remove the first IT company from the list
22. Remove the middle IT company or companies from the list
23. Remove the last IT company from the list
24. Remove all IT companies from the list
25. Destroy the IT companies list
26. Join the following lists:
27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
'''

lista_vacia = []

lista_con_mas_de_5 = [1, 2, 3, 4, 5, 6]

print(len(lista_con_mas_de_5))

primer_elemento = lista_con_mas_de_5[0]
elemento_medio = lista_con_mas_de_5[len(lista_con_mas_de_5) // 2]
ultimo_elemento = lista_con_mas_de_5[-1]
print(primer_elemento)
print(elemento_medio)
print(ultimo_elemento)

mixed_data_types = ['TuNombre', 25, 1.75, 'Soltero', 'TuDirección']

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print(it_companies)

print(len(it_companies))

print(it_companies[0])
print(it_companies[len(it_companies) // 2])
print(it_companies[-1])

it_companies[0] = 'Meta'
print(it_companies)
it_companies.append('Twitter')
print(it_companies)
it_companies.insert(len(it_companies) // 2, 'Salesforce')
print(it_companies)

'''
1. Find the middle country(ies) in the [countries list](https://github.com/Asabeneh/30-Days-Of-Python/tree/master/data/countries.py)
1. Divide the countries list into two equal lists if it is even if not one more country for the first half.
1. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
'''

paises = ['China', 'Rusia', 'USA', 'Finlandia', 'Suecia', 'Noruega', 'Dinamarca']

if len(paises) % 2 == 0:
    paises_medio = paises[(len(paises) // 2) - 1:(len(paises) // 2) + 1]
else:
    paises_medio = [paises[len(paises) // 2]]
print("País(es) del medio:", paises_medio)

if len(paises) % 2 == 0:
    primera_mitad = paises[:len(paises) // 2]
    segunda_mitad = paises[len(paises) // 2:]
else:
    primera_mitad = paises[:len(paises) // 2 + 1]
    segunda_mitad = paises[len(paises) // 2 + 1:]
print("Primera mitad:", primera_mitad)
print("Segunda mitad:", segunda_mitad)

primer_pais, segundo_pais, tercer_pais, *paises_escandinavos = paises
print("Primer país:", primer_pais)
print("Segundo país:", segundo_pais)
print("Tercer país:", tercer_pais)
print("Países escandinavos:", paises_escandinavos)

lista_vacia = []

lista_con_mas_de_5 = [1, 2, 3, 4, 5, 6]
print(len(lista_con_mas_de_5))

primer_elemento = lista_con_mas_de_5[0]
elemento_medio = lista_con_mas_de_5[len(lista_con_mas_de_5) // 2]
ultimo_elemento = lista_con_mas_de_5[-1]
print("Primer elemento:", primer_elemento)
print("Elemento medio:", elemento_medio)
print("Último elemento:", ultimo_elemento)

mixed_data_types = ['TuNombre', 25, 1.75, 'Soltero', 'TuDirección']

empresas_ti = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(empresas_ti)

print(len(empresas_ti))

print(empresas_ti[0])
print(empresas_ti[len(empresas_ti) // 2])
print(empresas_ti[-1])

empresas_ti[0] = 'Meta'
print(empresas_ti)
empresas_ti.append('Twitter')
print(empresas_ti)
empresas_ti.insert(len(empresas_ti) // 2, 'Salesforce')
print(empresas_ti)
