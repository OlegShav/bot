#Module b_2 Strings
#numbers = '1 2 3 4 5 6 7'
#numbers_split = numbers.split()
#numbers_join = ('\n').join(numbers_split)
#print(numbers_join)

#hours = 1
#minutes = 18
#seconds = 3
#print("%02d:%02d:%02d" % (hours, minutes, seconds))

#L = list(map(float, input().split()))
#L[0], L[-1] = L[-1], L[0]
#L.append(sum(L))
#print(L)

#d = {'day' : 22, 'month' : 6, 'year' : 2015}
#print("||".join(d.keys()))

#Задание 2.5.12
#sym = input()
#s = set(list(map(str, sym)))
#print(len(s))
# Ответ:
#text = input("Введите текст:")
#unique = list(set(text))
#print("Количество уникальных символов: ", len(unique))

#Задание 2.5.14
#a = input("Введите первую строку: ")
#b = input("Введите вторую строку: ")

#a_set, b_set = set(a), set(b) # используем множественное присваивание

#a_and_b = a_set.intersection(b_set)

#print(a_and_b)

#Задание 2.5.15
#a = input(int())
#b = input(int())
#a_split = a.split(' ')
#b_split = b.split(' ')
#a_set, b_set = set(a_split), set(b_split) # используем множественное присваивание
#a_and_b = a_set.symmetric_difference(b_set)
#print(a_and_b)

#L = ['a', 'b', 'c']
#print(id(L))

#L.append('d')
#print(id(L))

# a = 5
# b = 3+2
# print(id(a), id(b))

# password = "dgh36gh7"
# answer = input()
# print(password == answer)

#3.4.6

# number = str(input())
# pal = "".join(reversed(number))
# print("Number - палиндром") if number == pal else print("Number - не палиндром")
#3.5.6
# a = [5,3]
# b = [5,3]
# result = a is b
# print(result)

#3.5.ИТОГОВОЕ

# temperature = int(input("Введите температуру "))
# isRain = input("Есть дождь? ")
#
# if 20 <= temperature <= 30:
#     if isRain == "Нет":
#         print("Футболку и шорты")
#     else:
#         print("Футболку, шорты и дождевик")
# if temperature < 0:
#     print("Пуховик")
# else:
#     if isRain == "Нет":
#         print("Пальто")
#     else:
#         rain = input("Осадки сильные? ")
#         if rain == "Нет":
#             print("Пальто и дождевик")
#         else:
#             print("Пальто, резиновые запоги и зонт")

#3.6.1
# i = 0
# while 2 ** i < 10000:
#     i += 1
# print(i)

# i = 0
# while i < 5:
#     i += 1
# print(i)

#4.3.2
# def multi(*nums):
#     multi_ = 1
#     for n in nums:
#         multi_ *= n
#     return multi_
#
# print(multi(1, 2, 3))

#4.3.3
# def rec_(n):
#     if n == 1:
#         return 1
#     return n + rec_(n - 1)
# print(rec_(5))

#4.3.4
# def reverse_str(string):
#    if len(string) == 0:
#        return ''
#    else:
#        return string[-1] + reverse_str(string[:-1])
#
# reverse_str('test')

#4.3.5
def sum_n(N):
    if N < 10:
        return N
    else:
        return N % 10 + sum_n(N // 10)
print(sum_n(12345))