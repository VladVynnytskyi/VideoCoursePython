num = int(input("Your num: "))

if num == 5:        #!= < > <= >=
    print("Yes")
    if num == 5:
        print("5")
elif num == 6:
    print("6")
else:
    print("else")

Happy = True

if num > 5 and not Happy:  #дві умови мають виконуватися
    print("He is happy")

if not Happy:
    print("He is not happy")

if num > 5 or not Happy:  #одна з умов має виконуватися
    print("He is happy")

#Тернарний оператор

data = "info"
# if data == "info":
#     correct = True
# else:
#     correct = False

correct = True if data == "info" else False

print(correct)