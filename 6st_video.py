for i in range(11):     #змінні і ніяк не конфліктують
    print("El: ", i) 

for i in range(5, 16):      #від 5 до 15
    print("Elem: ", i) 

for i in range(5, 16, 2):       #2 це крок циклу тобто за кожне коло +2 
    print("Element: ", i) 

word = "Hi world"

print("\n\n")

for i in word:
    if i == 'w':
        print("У слові є w")

#cikle while

i = 0

while i < 7:
    print(i)
    i += 1      #Щоб не було безкінченого циклу


print("\n\n\n\n\n")

work = True

while work:
    inp = input("Write 'Stop' " )
    if inp == 'Stop':
        work = False
print("end sickle")

#Оператори в циклах

for i in range(1, 11):

    if i % 2 == 0:
        continue            #не виходить з циклу а пропоскає певно літерацію в данному випадку пропускає парні числа

    if i == 7:
        break       #якщо я хочу вийти з циклу до 7 елементу
    print("El ", i)

#оператор Else в циклах
print('\n\n\n')


for i in 'Hello world':
    if i == 'w':
        print('done')
        break
else:
    print('Not found')