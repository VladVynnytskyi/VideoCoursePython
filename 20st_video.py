#Декоратори функцій
import webbrowser


def  validator(func):                   #це і є декоратор функції
    def wrapper(url):
  #      print('Before')                 #тут може бути якийсь код який виводиться раніше
        if '.' in url:
            func(url)
        else:
            print('посилання не правильне')
        func(url)                          #тут виводитться сама ця функція
        print('After')                  #і тут виводиться щось піся цієї функції
    return wrapper

@validator                              # я до цієї функції додаю декоратор
def open_url(url):
    webbrowser.open(url)

open_url('https://pl.wikipedia.org/wiki/Wikipedia:Strona_g%C5%82%C3%B3wna')