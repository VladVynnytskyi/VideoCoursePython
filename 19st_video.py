#Спадкування, поліморфізм, інкапсуляція

#Спадкування

class build:
    year = None
    city = None
    def __init__(self, year, city):             #конструктор
        build.year = year
        build.city = city
#        self.get_info()
        
    def get_info(self):
        print('Year: ', self.year, ". City: ", self.city, sep=' ')
         
class school(build):                    #клас school спадковує все що є в класі build
    __pupils = None

    def __init__(self, year, city, pupils = 50):
        super(school,self).__init__(year, city)                #це значиитт що ми маємо всі парметри з класу school а цей клас має ці параметри з класу build
        self.pupils = pupils

    def get_info(self):                         #тут ми переписуємо метод і це і є поліморфізм
        super().get_info()                  #super() цим я звертаюся до головного класу щоб взяти звідти  get_info()
        print('Pupils: ',self.pupils)
    #тут можна додавати додаткову характеристику до класу 

class house(build):                    #клас school спадковує все що є в класі build
    pass 
    #тут можна додавати додаткову характеристику до класу 

class shop(build):                    #клас school спадковує все що є в класі build
    pass 
    #тут можна додавати додаткову характеристику до класу 

 
school = school(1999, 'Lviv')
school.__pupils = 500               #це називається інкапсуляція через те що я поставив __ перед змінною я вже не можу там нічого змінівати юуде виводитися те що я поставив за замовчуванням в цбому випадку 50
school.pupils = 500                 #але якщо я буду звертатися без __ то все буде переписуватися
school.get_info()

house = house(2001, "New York")
house.get_info()
shop = shop( 2994, 'Kiyv')


#не варто на пряму працювати з полями а варто через методи і конструктори