# number = int(input("Введите число"))

# if number ==7:
#    print("Вы ввели число 7")
# else:
#    print("Вы ввели другое число")


# age = 17

# if age >= 18:
#     print("ВЫ уже взрослый")
# else:
#     print("Вам еще нету 18 лет")


# number = 1

# if number == 5:
#     print("Отлично")
# elif number ==4:
#     print("Хорошо")
# elif number ==3:
#     print("Неплохо")
# elif number ==2:
#     print("Плохо")
# elif number ==1:
#     print("Очень плохо")
# else:
#     print("Вы ввели другое число")                


# age = int(input("Введите ваш возраст"))

# if age < 18:
#     print("Вы ребенок")
# elif 18 <= age <65:
#     print("Вы взрослый")
# elif 65 <= age <99:
#     print("Вы в уважаемом возрасте")
# elif age <= 100:
#     print("Вы прожили целый век")
# else:
#     print("Вы ввели отрицательное значение")       

         

# a = int(input("Введите 1 число"))
# b = int(input("Введите 2 число"))
# if a > b:
#     print("1 число больше 2")
# elif a < b:    
#     print("2 число больше 1")
# else:
#     print("2 числа равны между собой")    


# a = int(input("Введите 1 число"))
# b = 3
# if a >= b:
#     print("a больше b")
# elif a <= b: 
#     print(a+10)


# num = int(input("Введите число"))
# if num != 20:
#     print(num + 5)
# else:    
#     print(num - 10)


# num = int(input("Какую оценку вы сегодня получили"))
# if num == 5 or num == 4 or num == 3:
#     print("Все хорошо")
# elif num == 2 or num == 1:
#     print("Ничего страшного")
# else:
#     print("Вы ввели число, которого нету в списке")        


# age = int(input("Введите свой возраст"))

# if age <= 18 and age >0:
#     print("Я ребенок")
# elif age >= 18 and age <=30:
#     print("Я юноша") 
# elif age >= 31 and age <=65:
#      print("Я взрослый")
# else:
#     print("Я старик")       


# num = int(input("Введите номер месяца"))
# if num ==1:
#     print("январь")
# elif num ==2:
#     print("февраль")
# elif num ==3:
#     print("Март")
# elif num ==4:
#     print("Апрель")
# elif num ==5:     
#     print("Май")
# elif num ==6:
#     print("июнь")
# elif num ==7:
#     print("июль")
# elif num ==8:
#     print("август")
# elif num ==9:
#     print("сентябрь")
# elif num ==10:
#     print("октябр")
# elif num ==11:
#     print("ноябрь")
# elif num ==12:                            
#     print("декабрь")
# else:
#     print("Такого месяца нету")    


# a = int(input("Первое число"))   
# b = int(input("второе число"))   
# c = int(input("третье число"))

# if a<b and a>b:
#     print("a больше всех")
# elif b>b and b>c:
#     print("b больше всех")
# elif c>b and c>a:
#     print("c больше всех")
# else:
#     print("они равны")             




# Задание 3
# num = int(input("Введите номер месяца, что бы получить время года"))
# if num == 1 or num == 2 or num == 3:
#     print("Зима")
# elif num == 4 or num == 5 or num == 6:
#     print("Весна")
# elif num == 7 or num == 8 or num == 9:
#     print(Лето)
# elif num == 10 or num == 11 or num == 12:  
#     print(Осень)  
# else:
#     print("нету") 






# 13.11.2014


# list = [5,20,30,67,90]
# for x in list:
#     x=x*2
#     print(x)

 

# for i in range(0,1000):
#     print(i)



# sum = 0
# for x in range(0,56):
#     sum = sum + x
# print(sum)



# for i in range(100, 0, -3):
#     print(i)



# for i in range(0,101):
#     print(i)   



# for i in range(100,0,-1):
#     print(i)


# N = int(input("Число"))
# for N in range(1,N):
#     print(N)



# for i in range(0,100):
#     if i %2 != 0:
#         print(i)


# sum = 0
# for i in range(0,100):
#     sum = sum + i
# print(sum)


# A = int(input("Введите первое число"))
# B = int(input("Введите второе число"))
# for n in range (A,B):
#     print(n)


# word = input("Введите слово")
# for i in word:
#     print(i)


# i = 1
# while i <=100:
#     print(i)
#     i += 1


# year = 0
# weight = int(input("Введите ваш вес"))
# one_kg_moon = 0.165
# weight_moon = weight * one_kg_moon
# while year < 15:
#     year = year + 1
#     weight_moon = weight_moon + one_kg_moon
#     print(str(weight_moon) + "- Ваш вес через" + str(year) + "Года/лет")



# num1 = int(input("До кого"))
# i = 100
# while num1 <= i:
#     print(i)
#     i-=2



# num1 = int(input("От кого числа"))
# num2 = int(input("До кого числа"))
# summa = 0
# while num1 <= num2:
#     if num1 % 2 !=0:
#         summa = summa + num1
#     num1 = num1 + 1
# print("Сумма",summa)        



# i = 0
# while i <=100:
#     print("Дом")
#     i+=1


# N = int(input("Число"))
# i = 100

# while N < i:
#     print(i)
#     i-=3


# while True:
#     print("123")



# a = int(input())
# b = int(input())
# for i in range(a,b+1):
#     print(i)


# task 1
# for i in range(1,20):
#     if i %2 == 0:
#         print(i)


# task 2
# n = int(input("Введите число"))
# sum = 0
# for i in range(1,n+1):
#     sum = sum + i
# print(sum)


# task 3    
# a = int(input("Введите число"))
# for i in range(1,11):
#     print(f"{a} * {i} = {a*i}")


# task 4
# for i in range(50,100):
#     if i %2 != 0:
#         print(i)



# vowels = "аеёиоуыэюя"

# n = input("Введите")
# count = 0
# for i in n.lower():
#     if i in vowels:
#         count += 1

# print(f"гласных букв в строке: {count}")


# list=[2,3,123,123,356,True,54.23,]
# print (list[4]) #4


# list = [ 1,4,"print",8,9,"Hello",True]
# list.append("545")
# list.insert(1, "hello")
# list.pop(2)

# for i in list:
#     print(i)


# b = [1,4,"print",8,9,"Hello",True]
# b = b[:2] + b[3:]
# print(b)


# import random
# c = []
# i = 0
# while i < 10:
#     c.append(random.randint(0,1000))
#     i += 1
# print(c)


# dog = {
#     "name": "Бобик",
#     "age": 15,
#     "poroda": "Овчкарка"
# }
# dog["name"] = "Vova"

# print(dog)


# list=[1,2,3,4,5,6,7,8,9,10]
# print (list[4])

# import random
# list = []
# i = 0
# while i <10:
#     list.append(random.randint(0,1000))
#     i += 1
# print(list)    




# list = []
# i = 0
# while i <10:
#     num = int(input(f"Введите число = {i}"))
#     list.append(num)
#     i+=1
# print(list)    



# list = [1,2,3,4,5,6,7,8,9,10]
# list.pop(2)
# for i in list:
#     print(i)


# list = [1,2,3,4,5,7,8,9]
# list.insert(1, "Hello")
# for i in list:
#     print(i)




# 20.11.2024 #Test

#task 1
# list = [1,2,3,4,5,6,7,8,9,10]

# for i in list:
#     if i %2==0:
#         print(i)

#task 2
# list = [1,2,3,4,5,6,7,8,9,10]
# sum = sum(list)
# print(sum)


#task 3
# list = []
# i = 0
# while i <10:
#     num = int(input(f"Введите число = {i}       "))
#     list.append(num)
#     i+=1
# sum = sum(list)
# print(list)
# print(sum)



#task 4
# list = [12,2,3,4,5,1,7,8,9,10]
# min = min(list)
# print(min)


#task 5
# list = [1,2,3,4,5,6,7,8,9,10]
# list.reverse()
# print(list)



# def countFood():
#     a = int(input())
#     b = int(input())
#     print("Всего", a+b, "ШТ.")
# countFood()


# def count(a,b):
#     return a+b
# print(count(2,3))


# def cylinder():
#     r = float(input())
#     h = float(input())

#     side = 2 * 3.14 * r * h

#     circle = 3.14 * r**2

#     full = side + 2 * circle
#     return full

# square = cylinder()
# print(square)


#task 1
# def countFood():
#     a = input()
#     b = input()
#     print(a +""+b)

# countFood()


# #task 2
# def list(lst):
#     a = []
#     for i in lst:
#         if i not in a:
#             a.append(i)
#     return a
# print(list([1,2,2,3]))        



#task 3
# def square(a):
#     s = a**2
#     p = 4 *a
#     return s,p
# print(square(2))




#25.11.2024

# #task 1
# list = [1,2,3,4,5,6,7,8,9,10,22,44,234,124,578,758,0,234,548,123,12,342345,]    
# for i in list:
#     if i %2==0:
#         print(i)


#task 2
# def count ():

#     sum = 0
#     for i in range(1,n+1):
#         sum = sum + i
#     print(sum)
# n = int(input("Введите число"))
# count()


#task3
# list = [12,2,3,4,5,1,7,8,9,10]
# min = min(list)
# max = max(list)
# print(min,max)


#task 4
# n=int(input("Введите число = "))
# for i in range(1,11): 
#     print(f"{n}*{i} = {n*i}")



#task5
# def count(word):
#     vowels = "aeyuio"
#     vowels2 = "аеуыояию"
#     count = 0
#     word = word.lower()
#     for i in vowels or i in vowels2:
#         count += 1
#     print(count)
# count("hello")        





#task6
# def list(lst):
#     a = []
#     for i in lst:
#         if i not in a:
#             a.append(i)
#     print(a)
# list([1,2,3,4,5,23,1,2,3,4,6,7,8,5,4])    



