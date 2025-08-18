# Словники (dict)

person = {'name':'Alex', 'age': '15', 5: 12, True:'False', (3,4): 45}            #name це ключ (типу як індекс) Alex це зачення на індексі name

print(person)

person[5] = 'Five'

print(person[5])

print(person['age'])

person1 = dict(name = 'alex', age = 16)           #так теж можна записати словник 

print(person1['age'])

for i in person1:
    print(i)