# Операторы сравнения 
# Условные операторы 
# Логические операторы

# Операторы сравнения:
# <,>,==(равно),<=,>=,!=(не равно)
# num1=15
# num2=15
# result = num1 = num2
# print(result)

# stroka1 = 'h'
# print(ord(stroka1))
# stroka2 = 'a'
# print(ord(stroka2))
# result = stroka1>stroka2
# print(result)
# print(chr(109))

# bool -- True(1) or False(0)
 
# Условные операторы
# if
# elif
# else

# if<condition>:
#     если в if приходит True
#     <body if>
# elif <condition>:
#     <body>
# else:
#     <body>

# string=input('Enter smth:')
# if string == 'Hello':
#     print('Hello stranger!')
# elif string == 'Mercedes':
#     print('Mercedes-Benz S class')
# else:
#     print('Совпадений не найдено ')

# print('Код закончился')



# sign up 
# email = input('Enter your email:')
# password1 = input('Enter password:')
# password2 = input('Enter password confirmation:')

# if password1 != password2:
#     raise Exception('passwords don\'t match')
# else:
#     print('Successfully signed up')

# age = input('Enter your age: ')
# #  print(type(age))
# if age.isdigit():
#     age = int(age)
# else:
#     print('Введите корректные данные')
#     raise Exception('Value error')
# if age<18:
#     print(f'chuvak prihodi cherez {18-age} let/goda')
# else:
#     print('Vy podhodite po vozrastu')

#Логические операторы 
# 1. and -> логическое и
# 2. or -> логическое или
# 3. not -> логическое отрицание 

# my_age = 20 
# your_age = 18
# result =  (my_age == 20) and (your_age ==19)
# print(result)

# result = my_age > 18 or your_age == 20
# print(result)

# result = not my_age ==20
# print(result)

# is_user_google_user = True
# is_user_github_user = True
# is_user_age_greater_21 = False
# user_accounts_coins = 10000

# if is_user_google_user and is_user_github_user and (is_user_age_greater_21 or user_accounts_coins>5000):
#     print('You can enter the system mr John')
# else:
#     print('Sorry, you couldnt enter')







#DOMASHKAAAAAAAAAAAAAAA


# x = int(input('Enter number:'))
# if x >= 90:
#   print("Отлично ваша оценка 5")
# elif x >= 80:
#   print('Здорово ваша оценка 4')
# elif x >=70:
#   print('Хорошо ваша оценка 3')
# elif x >= 60:
#   print('Вам стоит подучить материал')
# else:
#   print('Вы не сдали экзамен')

# x = input('Введите число: ')
# y = input('Введите число: ')
# z = input('Введите число: ')
# if x<=y and x<z:
#   print(x)
# elif y<=x and y <=z:
#   print(y)
# elif z<= x and z<= y:
#   print(z)



# x = input('Введите число: ')
# y = input('Введите число: ')
# z = input('Введите число: ')
# if x == y == z:
#   print(3)
# elif x == y !=z:
#   print(2)
# elif x ==z !=y:
#   print(2)
# elif y == x != z:
#   print(2)
# elif y == z !=x:
#   print(2)
# elif z == x !=y:
#   print(2)
# elif z == y !=x:
#   print(2)
# elif x !=y!=z:
#   print(0)



# x = int(input('Введите число:'))
# y = int(input('Введите число:'))
# if x%y == 0:
#   print(int(x/y))
# elif x%y > 0:
#   print(x,'Не делится на',y)
#   print('Частное:',x//y)
#   print('Остаток:',x%y)


# count = 0
# x = (input('Ввод: '))
# if x == str():
#   print(int(x)+count)

# count = 0
# while True:
#   try:
#     print('Write the number')
#     number = int(input())
#     print(str(count)+ '-->'+str(number))
#     count = number
#   except Exception as e:
#     print(f'Write the number in integer type\nThe Error:n{e}')
  


# count = 0
# num = input('Write the number: ')
# if num.isdigit():
#   num=int(num)
#   print(num,'-->','count=',num)
# else:
#   print('Введите корректные данные')
#   raise Exception('Value error')



# count = 0
# number = input('Vvedite chislo: ')

# if number.isdigit():
#   count = int(number)
#   print(count)
#   print(type(count))
# else:
#   print('Vy vveli nekkorektnye dannye')
