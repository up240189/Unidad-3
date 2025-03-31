'''
### Exercises: Level 1

1. Declare a function _add_two_numbers_. It takes two parameters and it returns a sum.
2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates _area_of_circle_.
3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, _convert_celsius_to-fahrenheit_.
5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
6. Write a function called calculate_slope which return the slope of a linear equation
7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, _solve_quadratic_eqn_.
8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.

### Exercises: Level 2

1. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
2. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
3. Call your function _is_empty_, it takes a parameter and it checks if it is empty or not
4. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

### Exercises: Level 3

1. Write a function called is_prime, which checks if a number is prime.
2. Write a functions which checks if all items are unique in the list.
3. Write a function which checks if all the items of the list are of the same data type.
4. Write a function which check if provided variable is a valid python variable
5. Go to the data folder and access the countries-data.py file.
6. Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
7. Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
'''

def add_two_numbers(a, b):
    return a + b

import math

def area_of_circle(r):
    return math.pi * r * r

def add_all_nums(*args):
    suma = 0
    for arg in args:
        if not isinstance(arg, (int, float)):
            return "Todos los argumentos deben ser números."
        suma += arg
    return suma

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def check_season(month):
    seasons = {
        'Autumn': ['September', 'October', 'November'],
        'Winter': ['December', 'January', 'February'],
        'Spring': ['March', 'April', 'May'],
        'Summer': ['June', 'July', 'August']
    }
    for season, months in seasons.items():
        if month.capitalize() in months:
            return season
    return "Mes no válido."

def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

def solve_quadratic_eqn(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return "No hay soluciones reales."
    elif discriminante == 0:
        return -b / (2*a)
    else:
        sol1 = (-b + math.sqrt(discriminante)) / (2*a)
        sol2 = (-b - math.sqrt(discriminante)) / (2*a)
        return sol1, sol2

def print_list(lista):
    for item in lista:
        print(item)

def reverse_list(lista):
    reversa = []
    for item in lista[::-1]:
        reversa.append(item)
    return reversa

def evens_and_odds(num):
    evens = len([i for i in range(num + 1) if i % 2 == 0])
    odds = len([i for i in range(num + 1) if i % 2 != 0])
    return f"El número de pares es {evens}. El número de impares es {odds}."

def factorial(num):
    if num < 0:
        return "El número debe ser positivo."
    resultado = 1
    for i in range(1, num + 1):
        resultado *= i
    return resultado

def is_empty(param):
    return param == "" or param == [] or param is None

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_items_unique(lista):
    return len(lista) == len(set(lista))

def all_items_same_type(lista):
    return all(isinstance(item, type(lista[0])) for item in lista)

def is_valid_variable(variable):
    try:
        eval(f"{variable} = 1")
        return True
    except SyntaxError:
        return False