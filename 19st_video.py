#Спадкування, поліморфізм, інкапсуляція

#Спадкування

class build:
    year = None
    city = None
    def __init__(self, year, city):
        build.year = year
        build.city = city
        self.get_info()
        
    def get_info(self):
        print('Year: ', self.year, ". City: ", self.city, sep=' ')
         
class school(build):                    #клас school спадковує все що є в класі build
    pass 

class house(build):                    #клас school спадковує все що є в класі build
    pass 

class shop(build):                    #клас school спадковує все що є в класі build
    pass 

school = school(1999, 'Lviv')
house = house(2001, "New York")
shop = shop( 2994, 'Kiyv')