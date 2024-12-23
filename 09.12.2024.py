
import math
# n = input("Введите целое чсло-")
# try:
#     n = int(n)
#     print("good")
# except:
#     print("Введите число, а не текст")    
    
# print("Hello world")    


# n = int(input("pervoe"))
# a = int(input("vtoroe"))
# try:
#     result = n/a
#     print(result)
# except ZeroDivisionError:
#     print("na 0 nema")    

# try:
#    n = int(input("число"))
#    result = 10/n
#    print(result)
# except (ValueError, ZeroDivisionError) as e:
#    print(f"Ошибка следующая - {e}")  


# numbers = []
# for i in range(10):
#     try:
#         num = float(input(f"Введите чмсло ({i + 1}/10):"))
#         numbers.append(num)
#     except ValueError:
#         print("Ошибка Введите корректное числовое значение")
#         numbers.append(0)
# print(f"Ваш список чисел: {numbers}")
# squares = [num ** 2 for num in numbers]
# print(f"Квадраты чисел: {squares}")           



# data = ["25","aabc","hello","9","-3","55"]
# arr = []
# for i in data:
#    try:
#     numbers = int(i)
#     arr.append(numbers **2)
#    except ValueError:
#     print(f'"{i}"не явл числом')

# print(arr)


n = int(input("pervoe"))
a = int(input("vtoroe"))
try:
    result = n/a
    print(result)
except (ZeroDivisionError, ValueError) as e:
    print(f"Ошибка следующая - {e}") 



# numbers = [10,20,30,40,50]
# try:
#     i = int(input("Введи индекс"))
#     if 0 <= i < len (numbers):
#         print(numbers[i])
#     else:
#         print("ВВедите сущ индекс")
# except ValueError:
#     print("Введите число")            



# x = -5

# if x <0:
#     raise ValueError("Значение не может быть отриц")


# def check_number(num):
#     if num <0:
#         raise ValueError("Значение не может быть отриц")
#     return num ** 2
# try:
#     result = check_number(-3)
#     print(result)
# except ValueError as e:
#     print(f"Произошла ошибка: {e}")    



# password = input("Введите ваш пароль:")
# try:
#     if len(password)>8<20:
#         raise ValueError("Ошибка: пароль должен содержать хотя бы 8 символов")
    
#     special_characters = "!@#$%&?/\(){}[]"
#     found_special_char = False

#     for char in password:
#         if char in special_characters:
#             found_special_char = True
#             break

#     if not found_special_char:
#         raise ValueError("Ошбика: Пароль должен содержать хотя бы один спец символ")
        
#     print("Пароль успешно принят")

# except ValueError as e:
#     print       

# try:
#     age = int(input("Введи возраст"))
#     if age<0 or age>120:
#         print("Возраст должен быть в диапозоне")
#     else:
#         print(age)
# except ValueError:
#     print("Введите число")               


#dz
# def C_to_f(c: float)-> float:
#     return c * 9 / 5 + 32
# def c_to_k(c: float)-> float:
#     return c +273.15
# def f_to_c(f: float)-> float:
#     return(f - 32) * 5 / 9
# def k_to_c(k: float)-> float:
#     return k-273.15    

# if __name__=="__main__":
#     c = 40
#     print(f"{c}°C = {C_to_f(c)}°F")
#     print(f"{c}°C = {c_to_k(c)}K")

#     f = 77
#     print(f"{f}°F = {f_to_c(f)}°C")

#     k = 298.15
#     print(f"{k}K = {k_to_c(k)}°C")





