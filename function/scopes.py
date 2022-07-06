# Области видимости и пространство имен
# Built-in (Встроенная) - print, len, max, int
# Global (Глобальная)
# Enclosed (Нелокальная, nonlocal)
# local (Локальная область видимости)

# def print_list(some_list):
#     for i in some_list:
#         print(i)
# i = 'q'
# print_list([1,2,3,4,5])
# print(i)

# a = 10 #global
# print #built-in
# def hello(): #global
#     a = 'Hello world' #local
#     print(a, 'local inside at func')
# hello()
# print(a, 'global')

# x = 'global'
# print(x,'1') # 1 global

# def enclosed():
#     x = 'enclosed'
#     def local():
#         x = "local"
#         print(x,'3') #local
#     print(x,'2') #enclosed
#     local()
#     print(x,'4')
# enclosed()
# print(x,'5')

# a = 'str'
# def func():
#     print(a)
#     a = 5
# func()

# num = 10
# def func():
#     def inner_func():
#         print(num)
#     inner_func()
# func()

# var = 100 #global variable
# def increment():
#     var = var + 1 #Try to update a global variable(using increment -> var += 1)
# increment()

# global -> Позволяет изменять значение глобальной переменной находясь в локальной области видимости.

# nonlocal -> позволяет менять значение не локальной переменной находясь в локальной области видимости.

# var = 100

# def increment():
#     global var
#     var += 1
# increment()
# print(var)

# def counter():
#     num = 0
#     def incrementer():
#         nonlocal num
#         num += 1
#         return num
#     return incrementer
# c = counter()
# print(c)
# print(c())
# print(c())
# print(c())

# print(len(dir(__builtins__)))
# print(abs(-15)) #Стандартный вызов встроенной функции 
# abs = 15 #Переопределяю встроенное имя abs в глобальной области
# del abs
# print(abs(-15))

# x = [[1,2,3] , [3,3,5]]
# y = x[0]
# z = x[1]
# t = sum(y)
# m = sum(z)
# if t > m:
#     print(t)
# else:
#     print(m)

# list_ = [[1,2,3] , [3,3,5] , [5,6,5] , [12,3,34]]
# sums = []
# for x in list_:
#     sums.append(sum(x))
# print(sums)
# print(max(sums))

# res = max([sum(x) for x in list_ ])
# print(res)
#-----------------------------------------------------------------------------
# alice = [4 , 12 , 35]
# john = [5 , 12 , 31]
# a = 0
# j = 0
# if alice[0] > john[0]:
#     a +=1
# elif alice[0] < john[0]:
#     j += 1

# if alice[1] > john[1]:
#     a +=1
# elif alice[1] < john[1]:
#     j += 1

# if alice[2] > john[2]:
#     a +=1
# elif alice[2] < john[2]:
#     j += 1
# res = {'Alice' : a, 'John' : j}
# print(res)

# alice = [13, 15, 38]
# john = [5, 15, 50]
# def compareScores(a, j):
#     score_a = 0
#     score_j = 0
#     for i  in range(0, len(a)):
#         if a[i] > j[i]:
#             score_a += 1
#         elif j[i] > a[i]:
#             score_j += 1
#         else:
#             pass
#     return {'Alice' : score_a, 'John' : score_j}
# print(compareScores(alice,john))
# print(compareScores([54, 20, 10], [10, 35, 15]))

# str1 = 'pythoniiist'
# my_dict = {i: str1.count(i) for i in str1}
# print(my_dict)

# def check():
#     x = x*2
#     print(x)

# name = 'Sandy'
# def func_one():
#     name = 'Andy'
#     def func_two():
#         name = 'MAndy'
#         print(name)
#         print(locals())
#     func_two()
# func_one()

