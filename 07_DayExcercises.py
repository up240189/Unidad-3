'''
1. Find the length of the set it_companies
2. Add 'Twitter' to it_companies
3. Insert multiple IT companies at once to the set it_companies
4. Remove one of the companies from the set it_companies
5. What is the difference between remove and discard
6. Join A and B
7. Find A intersection B
8. Is A subset of B
9. Are A and B disjoint sets
10. Join A with B and B with A
11. What is the symmetric difference between A and B
12. Delete the sets completely
13. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
14. Explain the difference between the following data types: string, list, tuple and set
15. _I am a teacher and I love to inspire and teach people._ How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
'''

it_companies = {'Google', 'Apple', 'Microsoft', 'Amazon', 'Facebook'}
longitud_it_companies = len(it_companies)
print("Longitud de it_companies:", longitud_it_companies)

it_companies.add('Twitter')
print("Después de agregar 'Twitter':", it_companies)

it_companies.update(['IBM', 'Oracle', 'SAP'])
print("Después de agregar múltiples empresas:", it_companies)

it_companies.remove('Facebook')
print("Después de remover 'Facebook':", it_companies)

try:
    it_companies.remove('NoExistente')
except KeyError:
    print("Error: 'NoExistente' no está en el conjunto y remove lanzó un KeyError.")

it_companies.discard('NoExistente')
print("Después de usar discard con un elemento no existente:", it_companies)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
union_AB = A.union(B)
print("Unión de A y B:", union_AB)

interseccion_AB = A.intersection(B)
print("Intersección de A y B:", interseccion_AB)

es_subconjunto = A.issubset(B)
print("¿Es A un subconjunto de B?:", es_subconjunto)

son_disjuntos = A.isdisjoint(B)
print("¿Son A y B conjuntos disjuntos?:", son_disjuntos)

union_A_con_B = A.union(B)
union_B_con_A = B.union(A)
print("Unión de A con B:", union_A_con_B)
print("Unión de B con A:", union_B_con_A)

diferencia_simetrica_AB = A.symmetric_difference(B)
print("Diferencia simétrica entre A y B:", diferencia_simetrica_AB)

del A
del B

edades = [22, 19, 24, 25, 24, 25, 24]
edades_set = set(edades)
print("Longitud de la lista de edades:", len(edades))
print("Longitud del conjunto de edades:", len(edades_set))
print("¿Cuál es más grande?:", "Lista" if len(edades) > len(edades_set) else "Conjunto")

print("String: Es una secuencia de caracteres encerrada entre comillas.")
print("List: Es una colección ordenada de elementos que permite duplicados y es mutable.")
print("Tuple: Es una colección ordenada de elementos que permite duplicados pero es inmutable.")
print("Set: Es una colección desordenada de elementos únicos y es mutable.")

oracion = "I am a teacher and I love to inspire and teach people."
palabras_unicas = set(oracion.split())
print("Número de palabras únicas en la oración:", len(palabras_unicas))
