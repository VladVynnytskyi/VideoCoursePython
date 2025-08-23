 #модулі в пайтоні

import time
import datetime as dt
import sys, os              #так теж можна але пайтон каже щоб краще так не було
import platform 
import math 
from math import sqrt as s, ceil 

#sys, os, platform всі ці платворми потрібні для роботи з операційною системою або ж з користувачем

print(sys.path)             #буде виводити повний шлях де знаходиться цей файл 16st_video.py
print(os.name)              #будк виводити назву операційної системи 
print(platform.system())    #теж будк виводити назву операційної системи


#time.sleep(2)           #присипляє програму на 2 секунди
#print('Hello')          #і зараз зявиться hello через 2 секунди

print(dt.datetime.now().time())              #datetime.datetime.now() виводить повний час і дату разом, datetime.datetime.now().time() виводить тільки час вбо day типу день hour month

print(math.sqrt(9))                             # щоб знайти корінь

print(ceil(s(11)))                   #math.ceil для того щоб округлити

#власні модуля
import mymodule

mymodule.hi()
print(mymodule.name)
mymodule.add_3_nums(2, 3, 4)


#пакетний менеджер pip

import cowsay

cowsay.cow('Hello Vlad\n')

