# Словники (dict)

person = {'name':'Alex', 'age': '15', 5: 12, True:'False', (3,4): 45}            #name це ключ (типу як індекс) Alex це зачення на індексі name

print(person)

person[5] = 'Five'

print(person[5])

print(person['age'])

person1 = dict(name = 'alex', age = 16)           #так теж можна записати словник 

print(person1['age'])

print(person.items())         #це там де ключі і значення



for key, values in person.items():
    print(key, values, sep = ' - ')         #як вивести ключ і аргумент

for el in person.values():
    print(el)                               #video course time code 11:00

for el in person.keys():
    print(el)                               