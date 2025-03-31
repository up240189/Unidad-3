'''
### Exercises: Level 1

1. Writ a function which generates a six digit/character random_user_id.
2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).

### Exercises: Level 2

1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
3. Write a function generate_colors which can generate any number of hexa or rgb colors.

### Exercises: Level 3

1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
2. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
'''

import random

def random_user_id():
    caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choices(caracteres, k=6))

print(random_user_id())

def user_id_gen_by_user():
    num_caracteres = int(input("Número de caracteres: "))
    num_ids = int(input("Número de IDs: "))
    caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    ids = [''.join(random.choices(caracteres, k=num_caracteres)) for _ in range(num_ids)]
    return ids

print(user_id_gen_by_user()) 

def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"

print(rgb_color_gen())

def list_of_hexa_colors(n):
    hexa_colores = []
    for _ in range(n):
        color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
        hexa_colores.append(color)
    return hexa_colores

def list_of_rgb_colors(n):
    rgb_colores = [rgb_color_gen() for _ in range(n)]
    return rgb_colores

def generate_colors(tipo, n):
    if tipo.lower() == 'hexa':
        return list_of_hexa_colors(n)
    elif tipo.lower() == 'rgb':
        return list_of_rgb_colors(n)
    else:
        return "Tipo no válido."

print(generate_colors('hexa', 3))
print(generate_colors('rgb', 3))

def shuffle_list(lista):
    lista_mezclada = lista[:]
    random.shuffle(lista_mezclada)
    return lista_mezclada

print(shuffle_list([1, 2, 3, 4, 5]))

def unique_random_numbers():
    return random.sample(range(10), 7)

print(unique_random_numbers())
