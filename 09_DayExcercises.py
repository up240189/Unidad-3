'''
### Exercises: Level 1

1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

### Exercises: Level 2

1. Write a code which gives grade to students according to theirs scores:
2. Check if the season is Autumn, Winter, Spring or Summer. If the user input is:
3. The following list contains some fruits:

### Exercises: Level 3

1. Here we have a person dictionary. Feel free to modify it!
'''

def verificar_edad_conducir():
    edad = int(input("Ingresa tu edad: "))
    if edad >= 18:
        print("Tienes la edad suficiente para aprender a conducir.")
    else:
        print(f"Necesitas esperar {18 - edad} años más para aprender a conducir.")

verificar_edad_conducir()

def comparar_edades(mi_edad):
    tu_edad = int(input("Ingresa tu edad: "))
    if tu_edad > mi_edad:
        diferencia = tu_edad - mi_edad
        print(f"Tú eres {diferencia} año{'s' if diferencia > 1 else ''} mayor que yo.")
    elif tu_edad < mi_edad:
        diferencia = mi_edad - tu_edad
        print(f"Yo soy {diferencia} año{'s' if diferencia > 1 else ''} mayor que tú.")
    else:
        print("Tenemos la misma edad.")

comparar_edades(25)

def comparar_numeros():
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    if a > b:
        print(f"{a} es mayor que {b}")
    elif a < b:
        print(f"{a} es menor que {b}")
    else:
        print(f"{a} es igual a {b}")

comparar_numeros()

def asignar_calificacion():
    puntuacion = int(input("Ingresa tu puntuación: "))
    if 80 <= puntuacion <= 100:
        print("A")
    elif 70 <= puntuacion <= 79:
        print("B")
    elif 60 <= puntuacion <= 69:
        print("C")
    elif 50 <= puntuacion <= 59:
        print("D")
    elif 0 <= puntuacion <= 49:
        print("F")
    else:
        print("Puntuación inválida.")

asignar_calificacion()

def verificar_estacion():
    mes = input("Ingresa el mes: ").capitalize()
    if mes in ['Septiembre', 'Octubre', 'Noviembre']:
        print("Otoño")
    elif mes in ['Diciembre', 'Enero', 'Febrero']:
        print("Invierno")
    elif mes in ['Marzo', 'Abril', 'Mayo']:
        print("Primavera")
    elif mes in ['Junio', 'Julio', 'Agosto']:
        print("Verano")
    else:
        print("Mes inválido.")

verificar_estacion()

def verificar_fruta():
    frutas = ['plátano', 'naranja', 'mango', 'limón']
    fruta = input("Ingresa una fruta: ").lower()
    if fruta in frutas:
        print("Esa fruta ya está en la lista.")
    else:
        frutas.append(fruta)
        print("Lista modificada:", frutas)

verificar_fruta()

persona = {
    'primer_nombre': 'Asabeneh',
    'apellido': 'Yetayeh',
    'edad': 250,
    'país': 'Finlandia',
    'casado': True,
    'habilidades': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'dirección': {
        'calle': 'Space street',
        'código_postal': '02210'
    }
}

if 'habilidades' in persona:
    habilidad_intermedia = persona['habilidades'][len(persona['habilidades']) // 2]
    print("Habilidad intermedia:", habilidad_intermedia)

if 'habilidades' in persona:
    print("Tiene habilidad en Python:", 'Python' in persona['habilidades'])

if set(['JavaScript', 'React']) == set(persona['habilidades']):
    print("Es un desarrollador frontend")
elif set(['Node', 'Python', 'MongoDB']).issubset(persona['habilidades']):
    print("Es un desarrollador backend")
elif set(['React', 'Node', 'MongoDB']).issubset(persona['habilidades']):
    print("Es un desarrollador fullstack")
else:
    print("Título desconocido")

if persona['casado'] and persona['país'] == 'Finlandia':
    print(f"{persona['primer_nombre']} {persona['apellido']} vive en Finlandia. Está casado.")
