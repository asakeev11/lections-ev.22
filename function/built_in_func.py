#Встроенные функции
# input()
# print()
# str()
# sum()
# list()
# len()
# divmod()
# globals()
# locals()
# max()
# min() etc.

# map()
# filter()
# lambda
# enumerate()

    # Анонимные функции - lambda(такие же функции только без названия)
    # Lambda функции могут принимать сколько угодно аргументов, но всегда возвращают только одно выражение.

# def sum_args(a, b):
#     res = a + b
#     return res

# def sum_args1(a, b): return a + b
# print(sum_args(1, 2))
# print(sum_args1(1, 2))

# sum_arg = lambda a, b: a + b    
# print(sum_arg(1, 2))

# x = lambda a, b, c: a + b + c
# print(x(5,6,7))

# def myFunc(n):
#     return lambda a: a * n
# my_doubler = myFunc(2)
# my_tripler = myFunc(3)

# print(my_doubler(11))
# print(my_tripler(11))

# ls = ['def', 'Ivan', 'John', '', ' ']
# new_list = sorted(ls, key = len)
# print(new_list)

#-----------------------------------------------------------------
# map(function, Iterable) -> применяет функцию к каждому элементу последовательноти и возвращает mapobject(итератор) с результатами.

# Например,с помощью map можно выполнять преобразования элементов. Перевести все строки в верхний регистр:
# list_of_words = ['one', 'two', 'three', 'dict']
# result = list(map(str.upper, list_of_words))
# print(result)
# result1 = list(map(len, list_of_words))
# print(result1)

# ls = ['1', '2', '3', '4']
# result = list(map(int, ls))
# print(result)

# names = ['John',' Jamie', 'Sansa', 'Tirion', 'Aibek']
# result = list(map(lambda x :f'Hello mr/mrs {x}', names))
# print(result)

# nums = [1,2,3,4,5]
# nums2 = [100,200,300,400,500]
# result = list(map(lambda x, y: x * y, nums, nums2))
# print(result)

# dict_ = {1 : 2, 3 : 4, 5 : 6}
# result = dict(map(lambda items: (items[0], str(items[1])), dict_.items()))
# print(result)
#------------------------------------------------------------------------

# filter(function, Iterable) - применяет ко всем элементам iterable функцию которую мы передаем и возвращает filterobject(итератор)
#  с теми объектами, для которых функция вернула True.

# list_of_str = ['one', 'two', 'list', '', '100', '1', '50', 'John99']
# result = filter(str.isdigit, list_of_str)
# print(result)
# for x in result:
#     print(x)

# ls = [10, 11, 102, 213, 314, 515]
# result = list(filter(lambda x: x % 2 != 0, ls))
# print(result)
# list_of_words = ['John', 'one', 'two', 'list', 'makers', 'ev.22']
# def func(stroku):
#     if len(stroku) >= 4:
#         return True
#     else:
#         return False
# func(list_of_words)
# print(func)

# list_of_words = ['John', 'one', 'two', 'list', 'makers', 'ev.22']
# result = list(filter(lambda x: len(x) >= 4, list_of_words))
# print(result)

#---------------------------------------------------------------------------------------------
# enumerate(Iterable) 
# ls = ['str', 'srt2', 'str3']
# # i = 0
# # for x in ls:
# #     print(f'element: {x}, index: {i}')
# #     i += 1
# for i, x in enumerate(ls):
#     print(f'element: {x}, index: {i}')

# new_list = list(enumerate(ls))
# print(new_list)


#------------------------------------
# my_list =  ['m', 'a', 'k', 'e', 'r', 's']
# import functools
# new_word = functools.reduce(lambda x, y: x + y, my_list)
# print(new_word)
#------------------------------------

#zip(iterable) - Она соединяет каждый элемент итерируемых элементов между собой в тип дaнных tuple и возвращает это.  

# list1 = [1, 2, 3]
# list2 = [100, 200 ,300]

# result = list(zip(list1, list2))
# print(result)

# a = [1, 2, 3, 4, 5]
# b = [10, 20, 30, 40]
# c = [100, 200 ,300]
# res = list(zip(a,b,c))
# print(res)

# zip для создания словарей
# d_keys = ['hostname', 'location', 'vendor', 'model', 'IOS', 'IP']
# d_values = ['london_r1', '21 NEw', 'Cisco', 4451, 15.4, '192.80.1.0']
# res = dict(zip(d_keys, d_values))
# print(res)




# d_keys = ['hostname', 'location', 'vendor', 'model', 'IOS', 'IP']
# data = {
#     'r1' : ['london_r1', '21 NEw', 'Cisco', 4451, 15.4, '192.80.1.0'],
#     'r2' : ['london_r2', '2 NEw', 'Cisco', 4451, 15.4, '192.80.1.1'],
#     'sw1' : ['london_r1', '21 NEw', 'Cisco', 3851, '13.6.XE', '192.80.1.0']
    
    
# }
# london_data = {}
# for key in data.keys():
#     london_data[key] = dict(zip(d_keys, data[key]))
# print(london_data)
#------------------------------------------------------------------------------------------------
# all и any
# all -> возвращает True, если все элементы объекта истинна (или объект пустой)
# ls = [[1,2], 1, 'stroka', True]
# print(all(ls))

# ip = '10.255.a.01'
# result = all(i.isdigit() for i in ip.split('.'))
# print(result)

# any -> возвращает True, если хотя бы один элемент истинный

# ls = [0, 0, '', False]
# print(any(ls))

# def ignore_command(command):
#     '''
#     Функция проверяет есть ли в команде слова из списка ignore. True - если есть, False - если нет такого слова. 
#     '''
#     ignore = ['rm -rf', 'alias', 'reset']
#     for word in ignore:
#         if word in command:
#             return True
#     return False
# # print(ignore_command('sudo reset configurations'))
# command = 'sudo reset configurations'
# if ignore_command(command):
#     raise Exception('Invalid command')
# print('Vse ok')

# ignore = ['rm -rf', 'alias', 'reset']
# command = 'sudo reset configurations'
# if any([word in command for word in ignore]):
#     raise Exception('Invalid command')
# print('Vse ok!')

#----------------------------------------------------------------------------------
# from random import choices
# from string import ascii_letters, digits
# from itertools import repeat

# q_pass = int(input('Введите колво паролей: '))
# print({
#     f(choices(ascii_letters, k = 8), choices(digits, k = 8)) for f in repeat(lambda x, y: ''.join(set(x + y)), q_pass)
# })

# def func(arg1, arg2 = '1'):
#     print(arg1 , arg2)
# func(arg2 = '1', arg1 = '2')

