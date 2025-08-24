#OOП обєктно орієнтоване програмування
class Dog:
    name = None
    age = None                          #можна буде до обєкту додати вік і імя
    isHappy = None

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

dog1 = Dog()                #dog1 це перший наш обєкт

dog1.name = 'Skubby'
dog1.age = 3
dog1.isHappy = True

dog2 = Dog()

dog2.name = 'Bob'
dog2.age = 6
dog2.isHappy = False

print(dog1.name)
print(dog2.name)



dog1.set_data("Skuby", 4, True)             #через наш власний метод
dog2.set_data('Bob', 6, False )

print('\n\n\n\n\n\n')
 
dog1.get_data()
dog2.get_data()

#                                       це все на прикладі робота 
#поліморфізм - загальний функціонал що можна переписати для визначення робота наприклад
#інкапсуляція - броня або захист внутрішніх данних самого класу
#поле == змінна 
#метод == функція 
