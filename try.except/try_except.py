# Обработка исключений 
# Операторы: try...except

# Ошибки -> связанные с кодом
# SyntaxError
# IndentationError
# TabError

# Исключения -> Invalid values
# ZeroDivisionError
# ArithmeticError
# NameError
# IndexError
# KeyError
# ValueError
# ImportError
# BaseException #прородитель всех ошибок

#try ... except

# try:
#     <body try>
# except:
#     <body except>

# num1 = int(input('Введите число:'))
# print(num1)
# print('Очень важная строчка кода')
# try:
#     num1 = int(input('Введите число:'))
#     print(num1)
# except:
#     print('Vy vveli nekkorektnye dannye, ispravte eto!!!')

# print('Очень важная строчка кода')

# 1. import sys
# list_ = [1,2,3,4,5]
# index = int(input('Vvedite index:'))
# try:
#     res = list_[index]
#     print(res)
# except:
#     import sys
#     print(f'oops, we catch {sys.exc_info()[0]} error!')

# 2. Exception as e
# list_ = [1,2,3,4,5]
# index = int(input('Vvedite index:'))
# try:
#     res = list_[index]
#     print(res)
# except Exception as e:
#     print(f'oops, we catch {e.__class__} error')

# list_ = [1,2,3,4,5]
# try:
#     index = int(input('Vvedite index:'))
#     res = list_[index]
#     print(res)
# except (IndexError, ValueError):
#     print('Vy vveli incorrect index or invalid symbols!')

# list_ = [1,2,3,4,5]
# try:
#     index = int(input('Vvedite index:'))
#     res = list_[index]
#     print(res)
# except IndexError:
#     print('IndexError!!!')
# except ValueError:
#     print('ValueError!!!')

# else в try...except
# finally в try...except
# try:
#     <body>
# except:
#     <body>
# else:
#     <body> #Сработает если в операторе try не случилась ошибка
# finally:
#     <body>#Сработает при любом исходе

try:
    num1 = int(input('Enter:'))
    num2 = int(input('Enter:'))
    result = num1 / num2
except ZeroDivisionError:
    print('На 0 делит нельзя')
except ValueError:
    print('Invalid symbols!')
else:
    print(result)
finally:
    print('Код закончился!')
