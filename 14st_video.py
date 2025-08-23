#обробка вийнятків
num = None                              #None це значить що у змінній нічого немає

while num is None:                      #можна вводити ==, немає різниці
    try:
        num = int(input('Input your number: '))
        num += 5
        print(num)
    except ValueError:
        print('Ви ввели щось не те')

#ще один приклад
try:
    a = 10
    b = int(input("Your num: "))

    print(a/b)
except ValueError:
    print('Ви ввели щось не те')
except ZeroDivisionError:
    print('На нуль ділити не можна')

except Exception:                   # Exception це коли воно може зловити всі помилка
    print('Щось пішло не так')  
else:                                # буде виводитися якщо все спрацює правильно тобто не буде ніяких помилок,якщо спрацював код в трай
    print('Ти молодець!')
finally:                            #буде завжди виводится не залежно чи спрацював код в трай чи в ексепт
    print('Oh')