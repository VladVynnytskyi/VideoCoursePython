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
print('\n\n\n\n')
for el in person.values():                      #ми тут виводимо тільки значення тобто values
    print(el)                              
print('\n\n\n\n\n')
for el in person.keys():                    #ми тут будемо виводити виключно ключі
    print(el)                               

print('\n\n\n\n\n')
print(person.get('name'))
print('\n\n\n')
person.popitem()                #видаляє останній елемент
print(person)

person.pop(5)                   #видаляє елемент '5'

print(person)

person['bio'] = 'Text'          #додати новий елемент у кінець нашого словника

print(person)



person.clear()

print (person)

print('\n\n\n\n\n\n')


#Створення великого словника

people = {
    'user_1' : {
        'name' : 'John',
        'age' : 16,
        'address' : ("New York", 'Street', '562'),
        'grades' : {'Math': 5, "Physics": 3}
    },
    'user_2' : {
        'surname' : 'Vynnytskyi',
        'name' : 'Vlad',
        'age' : 18,
        'adress' : ("New York", 'Street', '562'),
        'grades' : {'Math': 5, "Physics": 5}
    }
}

print(people['user_1']['address'][1])       #тут я відкриваю юзера 1 потім його адрес і тоді 1 індекс тобто вулиця