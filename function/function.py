# def <name_of_function> (<>a,b#параметры)

# def <name_of_function>(<>a, b #параметры):
#     <body> #некий код, некая логика
#     <return> #возвращаем что то

# <name_of_function>(<5, 6> #аргументы)

# параметры функции - это у нас переменные, которые будет принимать наша функция ,для того что бы, мы смогли работать с данными которые передаются в эту функцию

#Аргументы - данные, которые мы передаем для параметров при вызове функции

# return - нужен для того чтобы функция что то возвращала и для того что бы могли работать с результатом действия функции
# return - является необязательным оператором(возващает None - если не указать return)

# ls = []
# result = ls.append(1)
# print(ls)
# print('Результат действия:',result)

# result1 = ls.pop()
# print(ls)
# print('Результат действия:',result1)

# def sumTwoNums(num1, num2): #параметры
#     result = num1 + num2
#     #print(result)
#     return result
# print(sumTwoNums(5, 5)) #аргументы

# def isEven(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False

# a = 10
# b = int(input('Enter num: '))

# print(isEven(5))
# print(isEven(a))
# print(isEven(b))

# def isEven1(num: int) -> bool:
#     '''
#     Наша функция проверяет является ли число, типа int, четным.
#     '''
#     if num % 2 == 0:
#         return True
#     return False
# isEven()
# isEven1()
# dir()

# words =  'Anna', 'Ded', 'Kabak', 'Kazak', 'Walaw', 'Ono'
# def get_polindrom(words: list) -> list:
#     """
#     Функция возвращает список из полиндромов
#     """
#     result = []
#     for word in words:
#         if word.lower() == word[::-1].lower():
#             result.append(word)
#     return resulton

# func()

#-------------------------------------------------------------------------------------------

#default params

# def print_welcome(name: str = 'User') -> str:
#     print(f'Welcome, {name}!')
# print_welcome()

# def getpercentage(money:float, period:int) -> float:
#     '''
#     Return final amount of money!
#     '''
#     if money < 30000:
#         raise Exception('Вы ввели некоректное количество денег, мин ставка 30к')
#     if period < 3:
#         raise Exception('Вы ввели некоректный срок для депозита, мин срок 3 года')
#     i = 0
#     while i < period:
#         money = money + (money * 0.1)
#         # money *1.1 
#         # money + (money / 100 * 10)
#         i +=1 # i = i + 1
#     return money

# money = float(input('Введите сумму денег: '))
# year = int(input('Введите срок вашего депозита: '))
# print(getpercentage(money,year))


# 'Hello world! My name is John, last name is Snow. Nice to meet you!'
# def get_reverse(name:str) -> str:
#     '''Returns reversed str'''
#     y = name.split(' ')
#     print(y)
#     res = ' '.join(y[::-1])
#     print(res)
#     return res
# get_reverse('Hello world! My name is John, last name is Snow. Nice to meet you!')


# def dictionary_func(di):
#   for i in di:
#     print(i)
# dict = {'a': 1, 'b' : 2, 'c' : 3}
# dictionary_func(dict)

# def func_(a,b,c = 3):
#         return a + b + c
# func_(1,2)
# print(func_)

def func(x , y , z):
    pass

