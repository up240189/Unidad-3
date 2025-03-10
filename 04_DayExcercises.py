'''
1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
3. Declare a variable named company and assign it to an initial value "Coding For All".
4. Print the variable company using _print()_.
5. Print the length of the company string using _len()_ method and _print()_.
6. Change all the characters to uppercase letters using _upper()_ method.
7. Change all the characters to lowercase letters using _lower()_ method.
8. Use capitalize(), title(), swapcase() methods to format the value of the string _Coding For All_.
9. Cut(slice) out the first word of _Coding For All_ string.
10. Check if _Coding For All_ string contains a word Coding using the method index, find or other methods.
11. Replace the word coding in the string 'Coding For All' to Python.
12. Change Python for Everyone to Python for All using the replace method or other methods.
13. Split the string 'Coding For All' using space as the separator (split()) .
14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
15. What is the character at index 0 in the string _Coding For All_.
16. What is the last index of the string _Coding For All_.
17. What character is at index 10 in "Coding For All" string.
18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
19. Create an acronym or an abbreviation for the name 'Coding For All'.
20. Use index to determine the position of the first occurrence of C in Coding For All.
21. Use index to determine the position of the first occurrence of F in Coding For All.
22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
28. Does '\'Coding For All' start with a substring _Coding_?
29. Does 'Coding For All' end with a substring _coding_?
30. '&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;' &nbsp;, remove the left and right trailing spaces in the given string.
31. Which one of the following variables return True when we use the method isidentifier():
32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
33. Use the new line escape sequence to separate the following sentences.
34. Use a tab escape sequence to write the following lines.
35. Use the string formatting method to display the following:
36. Make the following using string formatting methods:
'''

cadena1 = 'Thirty'
cadena2 = 'Days'
cadena3 = 'Of'
cadena4 = 'Python'
cadena_completa1 = cadena1 + ' ' + cadena2 + ' ' + cadena3 + ' ' + cadena4
print(cadena_completa1)

cadena5 = 'Coding'
cadena6 = 'For'
cadena7 = 'All'
cadena_completa2 = cadena5 + ' ' + cadena6 + ' ' + cadena7
print(cadena_completa2)

empresa = 'Coding For All'

print(empresa)

print(len(empresa))

print(empresa.upper())

print(empresa.lower())

print(empresa.capitalize())
print(empresa.title())
print(empresa.swapcase())

print(empresa[:6])

print('Coding' in empresa)

print(empresa.replace('Coding', 'Python'))

cadena8 = 'Python for Everyone'
print(cadena8.replace('Everyone', 'All'))

print(empresa.split())

cadena9 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(cadena9.split(', '))

print(empresa[0])

print(len(empresa) - 1)

print(empresa[10])

nombre1 = 'Python For Everyone'
acronimo1 = ''.join([palabra[0] for palabra in nombre1.split()])
print(acronimo1)

nombre2 = 'Coding For All'
acronimo2 = ''.join([palabra[0] for palabra in nombre2.split()])
print(acronimo2)

print(empresa.index('C'))

print(empresa.index('F'))

cadena10 = 'Coding For All People'
print(cadena10.rfind('l'))

oracion = 'You cannot end a sentence with because because because is a conjunction'
print(oracion.find('because'))

print(oracion.rindex('because'))

oracion2 = 'You cannot end a sentence with because because because is a conjunction'
inicio = oracion2.find('because')
final = oracion2.rfind('because') + len('because')
print(oracion2[inicio:final])

print(oracion.find('because'))

inicio2 = oracion2.find('because')
final2 = oracion2.rfind('because') + len('because')
print(oracion2[inicio2:final2])

print(empresa.startswith('Coding'))

print(empresa.endswith('coding'))

cadena11 = '  Coding For All  '
print(cadena11.strip())

print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

bibliotecas = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(bibliotecas))

print('Estoy disfrutando este desafío.\nMe pregunto qué sigue.')

print('Nombre\tEdad\tPaís\tCiudad')
print('Asabeneh\t250\tFinlandia\tHelsinki')

radio = 10
area = 3.14 * radio ** 2
print(f'El área de un círculo con radio {radio} es {area} metros cuadrados.')

num1 = 8
num2 = 6
print(f'{num1} + {num2} = {num1 + num2}')
print(f'{num1} - {num2} = {num1 - num2}')
print(f'{num1} * {num2} = {num1 * num2}')
print(f'{num1} / {num2} = {num1 / num2:.2f}')
print(f'{num1} % {num2} = {num1 % num2}')
print(f'{num1} // {num2} = {num1 // num2}')
print(f'{num1} ** {num2} = {num1 ** num2}')
