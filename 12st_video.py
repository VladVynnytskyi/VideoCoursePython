# function робота з функціями

def info(word):
#    pass                            #це значить що функція пуста і нічого не виводить

    print(word , end = '')                   #по замовчуванню end = '\n' типу перехід на новий рядок 
    print('!')

word = 'home'
info('hello')

print('\n\n\n\n')

def summa(a, b):
    res = a + b 
#    print("Your result: ", res)
    info(res)

a = int(input('Input your 1 num '))
b = int(input('Input your 2 num '))

summa(a,b)

print('\n\n\n\n')

def summa(a, b):
    res = a + b 
#    print("Your result: ", res)
    info(res)
    return res                          #воно повертає результат і тепер я можу цей результат записати у змінну res1


res1 = summa(4, 5)
print(res1)                 #буде виводити none бо немає що записати треба написати у функції return

print('\n\n\n\n\n\n\n\n')

#практичний приклад (мінімальний елемент)

nums1 = [1, 2, 3, 55, 32, 3, 1, -2, 0]
minim = nums1[0]

for i in nums1:
    if i < minim:
        minim = i


print(minim)