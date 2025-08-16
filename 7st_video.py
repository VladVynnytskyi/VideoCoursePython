#Cписки даних

nums = [5, 6, 7, 54, 0, 34]
nums[0] = 55
print(nums[3])

nums2 = [2, 6, 88, [4, 6, 'hjd', True]]

print(nums2[3][2])

nums2 = [2, 6, 88, [4, 6, 'hjd', True]]

print(nums2[-1][2])     #останій елеент цього списку

nums.append(45)     #додати в кінець списку
nums.insert(1, False)       #в першу комірку я ставлю фолс заміть 6
#nums.extend([nums2])        #якщо додати одразу декілька значень або інший список
nums.sort()                 #треба щоб у списку був оинаковий тип даннх false like 0 true like 1, це все по зростанню
nums.reverse()              # це якщо по спаданю але спочатку треба відсортувати або просто без сортування що виведе навпаки вміст спискуі
nums.pop()                  #delete last element
nums.remove(54)              #delete element in list (54)
print(nums.count(34))                #скільки елементів у списку з 34
print(len(nums))                    #скільки елементів у списку    

    
nums.clear()                #очищає список
print(nums) 


print("\n\n\n\n")

#Списки і цикли

nums = [2, 3, 65, 32, 1, 45]

for el in nums:                     #перерахування всіх елементів за жопомогою циклу range не потрібен
    print(el)

for el in nums: 
    res = el ** 2                   #можна робити різні дії  Наприклад підняти до квадрату
    print(res)

#Practice

user = int(input("Enter hobby numbers: "))
i = 0 
hobby=[]

while user > i:
    text = "Enter your " + str(i + 1) + " hobby: "
    tex = input(text)
    hobby.append(str)

    i += 1

print(hobby)