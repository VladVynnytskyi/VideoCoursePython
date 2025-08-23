#meneger with ... as

#try:
 #   file = open('data/file.txt', 'r')
#    print(file.read())
#except FileNotFoundError:
#    print('File not found')
#finally:
 #   file.close()                    #буде помилка бо файналі немає доступу до змінної file до неї має доступ тільки трай

#ось як це пофіксити тут знадобиться with as

try:
    with open('data/text.txt', 'r', encoding = 'utf-8') as file:        #encoding = 'utf-8' це значить що у файлі можна записувати і укр мовою і англ наприклад
        print(file.read())                          #ми це робили для того бо with автоматично закриває цей файл
except FileNotFoundError:
    print('File not found')