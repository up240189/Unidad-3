'''
1. Create an empty tuple
2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
3. Join brothers and sisters tuples and assign it to siblings
4. How many siblings do you have?
5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
6. Unpack siblings and parents from family_members
7. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
8. Change the about food_stuff_tp  tuple to a food_stuff_lt list
9. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
10. Slice out the first three items and the last three items from food_staff_lt list
11. Delete the food_staff_tp tuple completely
12. Check if an item exists in  tuple:
- Check if 'Estonia' is a nordic country
- Check if 'Iceland' is a nordic country

  ```py
  nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
  ```
'''
tupla_vacia = ()

hermanas = ('Ana', 'María', 'Isabel')
hermanos = ('Juan', 'Pedro', 'Carlos')

hermanos_y_hermanas = hermanas + hermanos

numero_de_hermanos = len(hermanos_y_hermanas)
print("Número de hermanos:", numero_de_hermanos)

padres = ('Padre', 'Madre')
miembros_de_familia = hermanos_y_hermanas + padres


*hermanos_desempaquetados, padre, madre = miembros_de_familia

frutas = ('manzana', 'banana', 'naranja')
verduras = ('zanahoria', 'lechuga', 'tomate')
productos_animales = ('huevo', 'leche', 'queso')
comida_tp = frutas + verduras + productos_animales

comida_lt = list(comida_tp)

medio_index = len(comida_lt) // 2
if len(comida_lt) % 2 == 0:
    elementos_del_medio = comida_lt[medio_index-1:medio_index+1]
else:
    elementos_del_medio = comida_lt[medio_index:medio_index+1]
print("Elemento(s) del medio:", elementos_del_medio)

primeros_tres = comida_lt[:3]
ultimos_tres = comida_lt[-3:]
print("Primeros tres elementos:", primeros_tres)
print("Últimos tres elementos:", ultimos_tres)

del comida_tp

paises_nordicos = ('Dinamarca', 'Finlandia', 'Islandia', 'Noruega', 'Suecia')
print("¿Estonia es un país nórdico?", 'Estonia' in paises_nordicos)
print("¿Islandia es un país nórdico?", 'Islandia' in paises_nordicos)
