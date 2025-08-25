#Конструктори, перевизначення методів#OOП обєктно орієнтоване програмування

#Конструктори

class Dog:
    name = None
    age = None                          #можна буде до обєкту додати вік і імя
    isHappy = None

    def __init__(self, name, age, isHappy):                 #це і є констріктор але він повинен називатися __init__ і має бути завжи мінімум self
        # self.name = name
        # self.age = age
        # self.isHappy = isHappy
        self.set_data(name, age, isHappy)
        print("You create the object")      #тепер кожного разу при створенні обєкту буде виводитися це 





#       pass                            #це значить що він пустий


    def set_data(self, dog_name, dog_age, dog_isHappy):                      #це метод а метод == функція але вона завжди буде приймати пареметр self
        self.name = dog_name
        self.age = dog_age
        self.isHappy = dog_isHappy
        print('name ', self.name)
        print(self.age)
        print(self.isHappy)
    def get_data(self):
        print(self.name, 'age: ', self.age, 'isHappy: ', self.isHappy)


#   pass                                #pass це значить що клас пустий

dog1 = Dog('Les', 4, True)                #dog1 це перший наш обєкт

# dog1.name = 'Skubby'
# dog1.age = 3
# dog1.isHappy = True

dog2 = Dog('Kon ', 5, False)

# dog2.name = 'Bob'
# dog2.age = 6
# dog2.isHappy = False

# print(dog1.name) 
# print(dog2.name)



# dog1.set_data("Skuby", 4, True)             #через наш власний метод
# dog2.set_data('Bob', 6, False )

# print('\n\n\n\n\n\n')
 
# dog1.get_data()
# dog2.get_data()

#                                       це все на прикладі робота 
#поліморфізм - загальний функціонал що можна переписати для визначення робота наприклад
#інкапсуляція - броня або захист внутрішніх данних самого класу
#поле == змінна 
#метод == функція 

#перевизначення методів             тут трохи погано працює але це через верхній клас і однакові назви
print('\n\n\n\n\n\n\n\n\n')

class Dog13:
    name = None
    age = None                         
    isHappy = None

    def __init__(self, name= 'bob', age = 1, isHappy = True):          # #якщо я не буду передавати третій параметр то він авоматично буде приймати True 

        self.set_data(name, age, isHappy)
        print("You create the object")      


 
    def set_data(self, dog_name = " bob", dog_age = 1, dog_isHappy = True):               #якщо я не буду передавати третій параметр то він авоматично буде приймати True
        self.isHappy = dog_isHappy
        print('name ', self.name)
        print(self.age)
        print(self.isHappy)
    def get_data(self):
        print(self.name, 'age: ', self.age, 'isHappy: ', self.isHappy)

dog1 = Dog13('Les', 4, True)              
dog1 = Dog13(age = 4)                   #якщо я хочу один параметр переписати а решта все буде за замовчуванням


dog2 = Dog13('Kon ', 5, False)

dog1.set_data('Alex ', 5)