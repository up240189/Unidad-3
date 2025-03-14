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
