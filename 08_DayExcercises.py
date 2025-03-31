'''
1. Create  an empty dictionary called dog
2. Add name, color, breed, legs, age to the dog dictionary
3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
4. Get the length of the student dictionary
5. Get the value of skills and check the data type, it should be a list
6. Modify the skills values by adding one or two skills
7. Get the dictionary keys as a list
8. Get the dictionary values as a list
9. Change the dictionary to a list of tuples using _items()_ method
10. Delete one of the items in the dictionary
11. Delete one of the dictionaries
'''

dog = {}

dog['name'] = 'Firulais'
dog['color'] = 'Marrón'
dog['breed'] = 'Pastor Alemán'
dog['legs'] = 4
dog['age'] = 5

print("Diccionario dog:", dog)

student = {
    'first_name': 'Juan',
    'last_name': 'Pérez',
    'gender': 'Masculino',
    'age': 20,
    'marital_status': 'Soltero',
    'skills': ['Python', 'Java'],
    'country': 'México',
    'city': 'Aguascalientes',
    'address': 'Calle Ficticia 123'
}

print("Diccionario student:", student)

print("Longitud del diccionario student:", len(student))

skills = student['skills']
print("Habilidades:", skills)
print("Tipo de datos de skills:", type(skills))

student['skills'].extend(['C++', 'SQL'])
print("Habilidades modificadas:", student['skills'])

keys = list(student.keys())
print("Claves del diccionario:", keys)

values = list(student.values())
print("Valores del diccionario:", values)

items = list(student.items())
print("Diccionario como lista de tuplas:", items)

del student['address']
print("Diccionario tras eliminar 'address':", student)

del dog
print("Diccionario dog eliminado.")
